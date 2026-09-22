import sqlite3

#дневник
connect = sqlite3.connect("store.db")

#рука и ручка
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (30) NOT NULL,
    price INT NOT NULL,
    quantity INT NOT NULL 
)
''')
connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )
    connect.commit()
    print('Товар добавлен')

def read_products():
    cursor.execute(
        'SELECT * FROM products'
    )
    data = cursor.fetchall()
    print(data)


def update_product(price, id):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, id)

    )
    connect.commit()
    print("Цена обновлен")

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (id,)
    )
    connect.commit()
    print('товар удален')
delete_product(6)
update_product(2000, 5)
read_products()
#create_product('CHARGER',1500, 12)

