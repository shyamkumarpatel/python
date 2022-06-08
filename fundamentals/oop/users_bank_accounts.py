class BankAccount:
    list_All_Back_Accounts = []
    
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.list_All_Back_Accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self,accountName, name):
        print(f'User {name} \tAccount: {accountName}', ' --> Balance: $'+str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*(self.int_rate/100)
        return self

    @classmethod
    def display_all_balance(cls):
        for account in cls.list_All_Back_Accounts:
            print('Balance: $'+str(account.balance))

class User:
    list_users = []
    def __init__ (self, name):
        self.name = name
        self.account = {'Checking':BankAccount(0, 0), 'Saving':BankAccount(1,0)}
        User.list_users.append(self)

    def make_deposit(self, amount, accountName):
        self.account[accountName].deposit(amount)
        return self

    def make_withdrawal(self, amount, accountName):
        self.account[accountName].withdraw(amount)
        return self
    
    def display_user_balance(self, accountName):
        self.account[accountName].display_account_info(accountName, self.name)
        return self

    def transfer_money(self, accountName, other_user, otherAccountName, amount):
        self.make_withdrawal(amount,accountName)
        other_user.make_deposit(amount,otherAccountName)



alfredo = User('Alfredo')
alfredo.make_deposit(100,'Checking').make_deposit(200,'Saving').make_deposit(300,'Checking').display_user_balance('Saving').make_withdrawal(25,'Checking').display_user_balance('Checking')

print('------------------------')
alfredo.transfer_money('Checking', alfredo, 'Saving',150)
alfredo.display_user_balance('Checking').display_user_balance('Saving')
print('------------------------')

winter = User('Winter')
winter.display_user_balance('Checking').display_user_balance('Saving')
print('------------------------')
alfredo.transfer_money('Saving', winter, 'Checking',150)

alfredo.display_user_balance('Checking').display_user_balance('Saving')
winter.display_user_balance('Checking').display_user_balance('Saving')