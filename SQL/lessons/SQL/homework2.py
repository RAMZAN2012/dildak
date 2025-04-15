class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")

    def start_engine(self):
        return "Двигатель заведен"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def info(self):
        super().info()
        print(f"Количество дверей: {self.doors}")
    
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def info(self):
        super().info()
        print(f"Тип мотоцикла: {self.bike_type}")

car = Car("BMW", "M5 F90 1st edition", 2017, 4)
bike = Bike("Yamaha", "R1", 2021, "Спорт")

print("Информация об автомобиле:")
car.info()
print(car.start_engine())

print("\nИнформация о мотоцикле:")
bike.info()
print(bike.start_engine())
