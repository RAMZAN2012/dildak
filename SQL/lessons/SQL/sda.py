import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (50)NOT NULL,
age INT DEFAULT NULL,
direction TEXT,
is_have BOOLEAN NOT NULL DEFAULT FALSE,
birth_date  DATE,
rating DOUBLE (4,2)DEFAULT(0.0)
        )
""")
def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input('ВВедите напрвление: ')
    is_have = bool(input('ВВедите наличие ноута: '))
    birth_date = (input('ВВедите дату рождения: '))
    rating = float(input("рейтинг"))

    cursor.execute(f"""INSERT INTO users
                (full_name, age, direction, is_have, birth_date, rating)
                VALUES(?,?,?,?,?,?),(full_name, age, direction, is_have, birth_date, rating)""")
    connect.commit()
def all_students():
    cursor.execute("SELECT * FROM users")
    students = cursor.fetchall()
    print(students)

def one_student(id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (id))
    students = cursor.fetchon()
    print(students)
def delete_student(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()
    print(f'Пользователь {id}, был успешно удалён')
# all_students()
# register()
# one_student(3)

delete_student(1)