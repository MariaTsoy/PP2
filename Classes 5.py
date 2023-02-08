class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdraw cannot exceed the available balance.")
            return
        else:
            self.balance -= amount


acc1 = Account("Maria", 2000)
acc2 = Account("Alibek", 50000)
acc3 = Account("Polina", 150)

print(acc1.balance)
acc1.deposit(3000)
print(acc1.owner, acc1.balance)

acc2.withdraw(51000)
print(acc2.balance)

acc3.deposit(50)
acc3.withdraw(200)
print(acc3.balance)
