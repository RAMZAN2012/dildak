import sqlite3

connect = sqlite3.connect("movie.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (50)NOT NULL
)
""")
def register():
    full_name = input("Введите ФИО: ")

    cursor.execute(f"""INSERT INTO users
                (full_name)
                VALUES(?)""",(full_name,))
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
    cursor.execute("DELETE FROM users WHERE id = ?", (id))
    connect.commit()
    print(f'Пользователь {id}, был успешно удалён')
all_students()
register()
one_student(3)
