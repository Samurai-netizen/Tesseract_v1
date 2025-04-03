import sqlite3
import json


def devDBinit():
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS ChatState (
            id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT NOT NULL,
            whid TEXT,
            article TEXT,
            amount INTEGER,
            buy_price_rmb INTEGER,
            margin INTEGER
            )
            ''')

            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def devDB_DROP():
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()

            cursor.execute('''
            DROP TABLE ChatState;
            ''')

            connection.commit()
            print("БД удалена")
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



def firstInit(id, name, state):
    whid = 1
    print(id, name, state)
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO ChatState (id, name, state, whid)
                VALUES(?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET state = ?;
            ''', (id, name, state, whid, state))
    except sqlite3.Error as e:
        print(f"Ошибка в firstInit: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    else:
        print("First init done")


def stateUpdate(id, name, state):
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO ChatState (id, name, state)
                VALUES(?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET state = ?;
            ''', (id, name, state, state))
    except sqlite3.Error as e:
        print(f"Ошибка в stateUpdate: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    else:
        print("Update state done")


def stateFetch(id):
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT state FROM ChatState WHERE id = ?;
            ''', (int(id),))
            state = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Ошибка в stateFetch: {e}")
        return None
    except Exception as e:
        print(f"Общая ошибка: {e}")
        return None
    else:
        print("Fetching state done")
        return state[0] if state else None


def newArticle(id, article):
    try:
        with sqlite3.connect('chat_state.db') as connection:
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
        print(f"Общая ошибка: {e}")
    else:
        print("Adding new 'article' done")

def newAmount(id, amount):
    try:
        with sqlite3.connect('chat_state.db') as connection:
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
        print(f"Общая ошибка: {e}")
    else:
        print("Adding new 'amount' done")


def fetchArgs(id):
    try:
        with sqlite3.connect('chat_state.db') as connection:
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

    except sqlite3.Error as e:
        print(f"Ошибка в fetchArgs: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    else:
        print("Fetch args done")
        print("Аргументы для вставки из Sqlite: ", article, amount)

        return article, amount #if args else None
