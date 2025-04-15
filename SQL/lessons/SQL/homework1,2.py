class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Автомобиль: {self.brand} {self.model}, {self.year} года выпуска."

    def is_old(self):
        from datetime import datetime
        current_year = datetime.now().year
        return (current_year - self.year) > 10

car1 = Car("Toyota", "Camiry", 2005)
car2 = Car("Tesla", "trash", 2020)

print(car1.info(), "- Старая?" , car1.is_old())
print(car2.info(), "- Старая?" , car2.is_old())