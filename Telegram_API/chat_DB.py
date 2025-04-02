import sqlite3

def devDBinit():
    connection = sqlite3.connect('chat_state.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ChatState (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def firstInit (id, name, state):
    connection = sqlite3.connect('chat_state.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO ChatState (id, name, state)
        VALUES(?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET state = ?;
    ''', (id, name, state, state))

    connection.commit()
    connection.close()
    print("First init done")


def stateUpdate (id, name, state):
    connection = sqlite3.connect('chat_state.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO ChatState (id, state)
        VALUES(?, ?)
        ON CONFLICT(id) DO UPDATE SET state = ?;
    ''', (id, state, state))

    connection.commit()
    connection.close()
    print("Update done")


def stateFetch (id):
    connection = sqlite3.connect('chat_state.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT state FROM ChatState WHERE id = ?;
    ''', (int(id),))

    state = cursor.fetchall()
    connection.commit()
    connection.close()
    print("Fetching state done")
    if state: return state[0]
