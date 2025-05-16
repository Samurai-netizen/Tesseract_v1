import sqlite3
import json
from config import HEADERS, SQLite_ADDRESS


def devDBinit():
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS ChatState (
            id INTEGER PRIMARY KEY,
            client_id TEXT,
            name TEXT,
            state TEXT NOT NULL,
            iddict TEXT,
            whid TEXT,
            article TEXT,
            amount INTEGER,
            buy_price_rmb INTEGER,
            margin INTEGER,
            sku TEXT
            )
            ''')

            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка в devDBinit: {e}")

def devDB_DROP():
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()

            cursor.execute('''
            DROP TABLE ChatState;
            ''')

            connection.commit()
            print("БД удалена")
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка в devDB_DROP: {e}")



def firstInit(id, name, state):
    print(id, name, state)
    client_id = HEADERS['Client-Id']
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO ChatState (id, client_id, name, state)
                VALUES(?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET state = ?, name = ?, client_id = ?;
            ''', (id, client_id, name, state, state, name, client_id))
    except sqlite3.Error as e:
        print(f"Ошибка в firstInit: {e}")
    except Exception as e:
        print(f"Общая ошибка блока firstInit: {e}")
    else:
        print("First init done")


def stateUpdate(id, name, state):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO ChatState (id, name, state)
                VALUES(?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET state = ?;
            ''', (id, name, state, state))
    except sqlite3.Error as e:
        print(f"Ошибка в stateUpdate: {e}")
    except Exception as e:
        print(f"Общая ошибка блока stateUpdate: {e}")
    else:
        print("Update state done")


def stateFetch(id):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT state FROM ChatState WHERE id = ?;
            ''', (int(id),))
            state = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Ошибка в stateFetch: {e}")
        return None
    except Exception as e:
        print(f"Общая ошибка блока stateFetch: {e}")
        return None
    else:
        print("Fetching state done")
        return state[0] if state else None


def fetchTelegramID(client_id):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                   SELECT id FROM ChatState WHERE client_id = ?;
                   ''', (client_id,))
            result_row = cursor.fetchone()
            result = result_row[0] if result_row else None
            print("result: ", result)

    except sqlite3.Error as e:
        print(f"Ошибка в fetchTelegramID: {e}")
    except Exception as e:
        print(f"Общая ошибка блока fetchTelegramID: {e}")
    else:
        print("Fetch user's Telegram ID done")
        print("Telegram id: ", result)

        return result #if args else None


def fetchArticle(client_id, sku):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
               SELECT iddict FROM ChatState WHERE id = ?;
               ''', (int(client_id),))
            result = cursor.fetchone()

            if not (result is None or not result[0]):  # Если есть запись
                iddict = json.loads(result[0])
                article = iddict[sku]
                print("iddict", iddict)

            if result is None or not result[0]:
                raise Exception("В базе данных либо ещё нет пар ключ-значение, либо что-то сломалось в fetchArticle")

    except sqlite3.Error as e:
        print(f"Ошибка sqlite в fetchArticle: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в fetchArticle: {e}")
    except Exception as e:
        print(f"Общая ошибка блока fetchArticle: {e}")
    else:
        print("Fetching article done (2/2)")

        return article

def fetchSku(id, article):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
               SELECT iddict FROM ChatState WHERE id = ?;
               ''', (int(id),))
            result = cursor.fetchone()

            if not (result is None or not result[0]):  # Если есть запись
                iddict = json.loads(result[0])
                sku = next((key for key, value in iddict.items() if value == article), None)
                sku = sku.replace("'", "")
                print("SKU:", sku)

            if result is None or not result[0]:
                raise Exception("В базе данных либо ещё нет пар ключ-значение, либо что-то сломалось в fetchSku")

    except sqlite3.Error as e:
        print(f"Ошибка sqlite в fetchSku: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в fetchSku: {e}")
    except Exception as e:
        print(f"Общая ошибка блока fetchSku: {e}")
    else:
        print("Fetching sku by article done (2/2)")

        return sku


def newArticle(id, article):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE ChatState
                SET article = ?
                WHERE id = ?;
            ''', (article, id))
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка в newArticle: {e}")
    except Exception as e:
        print(f"Общая ошибка блока newArticle: {e}")
    else:
        print("Adding new 'article' done")

def newAmount(id, amount):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE ChatState
                SET amount = ?
                WHERE id = ?;
            ''', (amount, id))
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка в newAmount: {e}")
    except Exception as e:
        print(f"Общая ошибка блока newAmount: {e}")
    else:
        print("Adding new 'amount' done")


def fetchArgs(id):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                   SELECT article FROM ChatState WHERE id = ?;
                   ''', (int(id),))
            article_row = cursor.fetchone()
            article = article_row[0] if article_row else None
            cursor.execute('''
                   SELECT amount FROM ChatState WHERE id = ?;
                   ''', (int(id),))
            amount_row = cursor.fetchone()
            amount = amount_row[0] if amount_row else None
            connection.row_factory = sqlite3.Row
            cursor.execute('''
                   SELECT iddict FROM ChatState WHERE id = ?;
                   ''', (int(id),))
            result = cursor.fetchone()
            #result = result_row[0] if result_row else None
            #print("result: ", result)
            #print("Type: ", type(result))

            if not (result is None or not result[0]):  # Если есть запись
                iddict = json.loads(result[0])
                sku = iddict[article]
                #print("iddict", iddict)
                #print("sku", sku)
                #print("article: ", article)

            if result is None or not result[0]:
                raise Exception("В базе данных ещё нет пар ключ-значение")

    except sqlite3.Error as e:
        print(f"Ошибка в fetchArgs: {e}")
    except Exception as e:
        print(f"Общая ошибка блока fetchArgs: {e}")
    else:
        print("Fetch args done")
        print("Аргументы для вставки из Sqlite: ", article, amount, sku, iddict)

        return [article, amount, sku] #if args else None


def newSKUaddChatdb(id, article):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE ChatState
                SET article = ?
                WHERE id = ?;
            ''', (article, id))
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка в newSKUbond: {e}")
    except Exception as e:
        print(f"Общая ошибка блока newSKUaddChatdb: {e}")
    else:
        print("Adding article for new pair article-SKU done (1/2)")


def newSKUbond(id, sku):
    try:
        with sqlite3.connect(SQLite_ADDRESS) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('''
               SELECT article FROM ChatState WHERE id = ?;
               ''', (int(id),))
            article_row = cursor.fetchone()
            article = article_row['article'] if article_row else None
            print("Article:", article)

            cursor = connection.cursor()
            cursor.execute('''
               SELECT iddict FROM ChatState WHERE id = ?;
               ''', (int(id),))
            result = cursor.fetchone()

            if not (result is None or not result[0]): # Если есть запись
                iddict = json.loads(result[0])
                article = iddict[article]
                print("iddict", iddict)

            if result is None or not result[0]: # Если нет записи
                print("Запись не найдена или iddict пуст.")
                iddict = {}

            print("Article для SKU", article)

            iddict[article] = sku
            print("Обновленный iddict", iddict)

            cursor.execute('''
                UPDATE ChatState
                SET iddict = ?
                WHERE id = ?
            ''', (json.dumps(iddict), id))
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка sqlite в newSKUbond: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в newSKUbond: {e}")
    #except Exception as e:
        #print(f"Общая ошибка блока newSKUbond: {e}")
    else:
        print("Adding new pair article-SKU done (2/2)")
