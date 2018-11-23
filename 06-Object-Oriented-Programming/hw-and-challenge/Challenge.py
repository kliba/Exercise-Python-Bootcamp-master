# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
#   owner
#   balance
# and two methods:
#   deposit
#   withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, income):
        print('Balance before transfer: ' + str(self.balance) + ', After the transaction: ' + str(self.balance + income))
        self.balance += income
        return self.balance

    def withdraw(self, outcome):
        if self.balance - outcome < 0:
            print("Your account is not allowed to be overdrawn")
            return self.balance
        else:
            print('Balance before withdraw: ' + str(self.balance) + '. Current balance:' + str(self.balance - outcome))
            self.balance -= outcome
            return self.balance

# 1. Instantiate, the class


acc = Account('Rikardo', 100)

# 2. Print the object


print(acc)

# 3. Show the account owner attribute


print(acc.owner)

# 4. Show the account balance


print(acc.balance)

# 5. Make a series of deposits and withdrawals


acc.deposit(50)
acc.withdraw(75)
print(acc.balance)
# 6. Make a withdrawal that exceeds the available balance


acc.withdraw(1200)
print(acc.balance)
