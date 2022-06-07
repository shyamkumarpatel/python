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
            

account1 = BankAccount(1, 0)
account2 = BankAccount(2, 0)

account1.deposit(100).deposit(200).deposit(300).display_account_info()

account2.deposit(200).deposit(300).withdraw(.12).withdraw(5.89).withdraw(6.98).withdraw(145.5).yield_interest().display_account_info()

BankAccount.display_all_balance()