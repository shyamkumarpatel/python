class User:
    list_users = []
    def __init__ (self, name):
        self.name = name
        self.amount = 0.0
        User.list_users.append(self)

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(self.amount)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

alfredo = User('Alfredo')
alfredo.make_deposit(100)
alfredo.make_deposit(25)
alfredo.make_deposit(50)
alfredo.make_withdrawal(2.78)
print(alfredo.name,end=' --> ')
alfredo.display_user_balance()

winter = User('Winter')
winter.make_deposit(150)
winter.make_deposit(50)
winter.make_withdrawal(2.85)
winter.make_withdrawal(23.78)
print(winter.name,end=' --> ')
winter.display_user_balance()

pablo = User('Pablo')
pablo.make_deposit(50)
print(pablo.name,end=' --> ')
pablo.display_user_balance()
pablo.make_withdrawal(2.85)
print(pablo.name,end=' --> ')
pablo.display_user_balance()
pablo.make_withdrawal(14.78)
print(pablo.name,end=' --> 45 ')
pablo.display_user_balance()
pablo.make_withdrawal(23.78)
print(pablo.name,end=' --> 48 ')
pablo.display_user_balance()

alfredo.transfer_money(winter, 50)
print(alfredo.name,end=' --> ')
alfredo.display_user_balance()
print(winter.name,end=' --> ')
winter.display_user_balance()

winter.make_deposit(100).make_deposit(200).make_deposit(300).display_user_balance().make_withdrawal(50).display_user_balance()