class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} зачислено на счёт.")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} снято со счёта.")
        else:
            print("Недостаточно средств.")

    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")

account = BankAccount("Анна")
account.show_balance()
account.deposit(1000)
account.withdraw(300)
account.show_balance()
account.withdraw(800)