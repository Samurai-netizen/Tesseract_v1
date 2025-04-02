import sqlite3


def devDBinit():
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS ChatState (
            id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT NOT NULL
            )
            ''')

            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def firstInit(id, name, state):
    try:
        with sqlite3.connect('chat_state.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO ChatState (id, name, state)
                VALUES(?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET state = ?;
            ''', (id, name, state, state))
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
        print("Update done")


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
