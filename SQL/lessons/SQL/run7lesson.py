from niga7 import User, UserService

user = UserService()

user_services = User(name = "Ramzan2012zver", email='asa@gmail.com', age = 12)

find = user.find_user_by_email('sosal@gmail.com')
if find:
    print(f'user was found: {find.name},{find.email} {find.age}')

delete = user.delete_user_by_email('sosal@gmail.com')
