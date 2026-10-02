class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= amount

cuenta = BankAccount(100)
cuenta.deposit(50)
cuenta.withdraw(30)
print(cuenta.balance)  # 120
cuenta.withdraw(1000)  # Fondos insuficientes