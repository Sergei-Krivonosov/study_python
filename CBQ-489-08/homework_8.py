#Task 1

class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            print('Недостаточно средств!')
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

# account = BankAccount('Maria', 1000)
# account.deposit(1000)
# account.withdraw(100)
# account.withdraw(100)
# account.withdraw(100)
# account.withdraw(100)
# account.withdraw(100)
#
# print(account.get_balance())




#Task2


class OverdraftAccount(BankAccount):

    def withdraw(self, amount):
        #if self._balance <= amount:
            self._balance -= amount

jack_account = OverdraftAccount('jack', 1000)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())