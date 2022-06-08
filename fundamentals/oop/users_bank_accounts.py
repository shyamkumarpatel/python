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

    def display_account_info(self):
        print('Balance: $'+str(self.balance))
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
        self.account = BankAccount(0, 0)
        User.list_users.append(self)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)



alfredo = User('Alfredo')
alfredo.make_deposit(100).make_deposit(200).make_deposit(300).display_user_balance().make_withdrawal(50).display_user_balance()