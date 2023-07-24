class SavingsAccount:

    users = 0
    last_transactions = {}

    def __init__(self, name, lastname, id):
 
        self.name = name
        self.lastname = lastname
        self.id = id

        self.savings = 0
        self.debt = 0
        self.full_name = self.name + ' ' + self.lastname

        SavingsAccount.users += 1
        self.id = SavingsAccount.users 

    def deposit(self, amount):

        if amount < 0:
            raise ValueError('You cannot deposit a negative amount of money.')
        else:
            self.savings += amount
            SavingsAccount.last_transactions[self.full_name + '_deposit'] = amount
            return '\nSuccesfully deposited ${amount} in your savings account.\nYour current savings are ${savings}\n'.format(amount = amount, savings = self.savings)

    def withdrawal(self, amount):
        if (self.savings <= 0 or amount > self.savings):
            message = '\nYou don\'t have enough funds for this action.\n'
        else:
            self.savings -= amount
            message = '\nSuccesfully withdrew ${amount} from your savings account.\nYour current savings are ${savings}\n'.format(amount = amount, savings = self.savings)
            SavingsAccount.last_transactions[self.full_name + '_withdrawal'] = amount

        return message

    def loan(self, amount):
        
        if self.debt > 100000:
            raise ValueError('Client has a debt that has to be paid before asking for another loan!')
        else:
            message = '\nSuccesfully loaned ${amount} from the bank.\nYour current debt is ${savings}\n'.format(amount = amount, savings = self.debt)
            self.debt += amount
            SavingsAccount.last_transactions[self.full_name + '_loan'] = amount
        return message

    def transfer(self, amount, user, rate = 0.05):
        transfer_fee = self.savings*rate
        if amount <= 0:
            raise ValueError('Invalid amount or not enough funds.')
        elif amount > self.savings:
            raise ValueError('You don\'t have enough funds for this action.')
        else:
            self.savings -= amount
            self.savings -= transfer_fee
            user.savings += amount
            SavingsAccount.last_transactions[self.full_name + '_transfer'] = amount
            message = '\n{user_1} succesfully transfered ${amount} to {user_2}.\nYour current savings are: ${savings}\n'.format(amount = amount, user_1 = self.full_name, user_2 = user.full_name, savings = self.savings)

        return message
    
    def pay_loans(self):
        if self.savings >= self.debt:
            self.savings -= self.debt
            self.debt = 0
            return 'You succesfully paid your debt!'
        else:
            raise ValueError('You don\'t have enough funds for this action.')
    
    def interests(self):
        earned_interests = 0.02*self.savings
        self.savings += earned_interests
        return self.savings

    def __repr__(self):
        return '\nWelcome to User Bank, {username}! Your current savings are ${savings}.\nYou owe the bank ${debt}\n'.format(username = self.full_name, savings = self.savings, debt = self.debt)
    

client_1  = SavingsAccount('Chocomilo','Kongzilla', 1000612467)
client_2  = SavingsAccount('Monky','Oso', 1000612466)
client_3  = SavingsAccount('Callita','Oso', 1000612465)
client_4  = SavingsAccount('Teddy','Oso', 1000612465)
client_5 = SavingsAccount('Bob', 'Corleone', 1000612464)


print(client_1.deposit(10000))
print(client_1.withdrawal(100))
print(client_2.deposit(50000))
print(client_2.withdrawal(1300))
print(client_3.deposit(10000))
print(client_3.transfer(5000, client_1))
print(client_4.deposit(10000))
print(client_5.deposit(10000))
print(client_5.loan(10000))