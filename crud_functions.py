import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    title = ['Vitamins A', 'Vitamins B', 'Vitamins C', 'Vitamins D']
    description = ['Описание 1', 'Описание 2', 'Описание 3', 'Описание 4']
    price = ['100', '200', '300', '400']

    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[0]}', f'{description[0]}', f'{price[0]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[1]}', f'{description[1]}', f'{price[1]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[2]}', f'{description[2]}', f'{price[2]}'))
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'{title[3]}', f'{description[3]}', f'{price[3]}'))

    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


initiate_db()


def add_user(username, email, age):
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    new_user = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0] + 1
    cursor.execute(f'''INSERT INTO Users VALUES('{new_user}', '{username}', '{email}', '{age}', '1000')''')
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    if check_user is None:
        return False
    connection.commit()
    return True


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    db = cursor.fetchall()
    return list(db)