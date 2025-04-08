import sqlite3

connect = sqlite3.connect("orders.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (50)NOT NULL,
product TEXTNOT NULL,
quantity INT NOT NULL
    )
""")
def register():
    name = input("Введите ФИО клиента: ")
    quantity = int(input("Введите кол-во товара: "))
    product = input("название товара: ")

    cursor.execute("""INSERT INTO orders
                    (name, product, quantity)
                    VALUES(?,?,?) (name, quantity, product)""")
    connect.commit()

def all_clients():
    cursor.execute("SELECT * FROM orders")
    clients = cursor.fetchall()
    print(clients)

def one_client(id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (id))
    clients = cursor.fetchon()
    print(clients)
def delete_client(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()
    print(f'Пользователь {id}, был успешно удалён')
# all_clients()
register()
# one_client(3)

# delete_client(1)