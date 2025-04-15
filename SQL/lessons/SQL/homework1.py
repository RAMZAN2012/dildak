class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}.")

# Примеры использования
person1 = Person("Андрей228", 30, "Огайо")
person2 = Person("БогдашаПицца", 25, "Санкт-Петербург52")
person3 = Person("ВаняЛягушка", 40, "3-9 Царство 3-10 государство")

person1.introduce()
person2.introduce()
person3.introduce()