class User:
    list_users = []
    def __init__ (self, name):
        self.name = name
        self.amount = 0.0
        User.list_users.append(self)

    def make_deposite(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount
    
    def display_user_balance(self):
        print(self.amount)

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposite(amount)

alfredo = User('Alfredo')
alfredo.make_deposite(100)
alfredo.make_deposite(25)
alfredo.make_deposite(50)
alfredo.make_withdrawal(2.78)
print(alfredo.name,end=' --> ')
alfredo.display_user_balance()

winter = User('Winter')
winter.make_deposite(150)
winter.make_deposite(50)
winter.make_withdrawal(2.85)
winter.make_withdrawal(23.78)
print(winter.name,end=' --> ')
winter.display_user_balance()

pablo = User('Pablo')
pablo.make_deposite(50)
pablo.make_withdrawal(2.85)
pablo.make_withdrawal(14.78)
pablo.make_withdrawal(23.78)
print(pablo.name,end=' --> ')
pablo.display_user_balance()

alfredo.transfer_money(winter, 50)
print(alfredo.name,end=' --> ')
alfredo.display_user_balance()
print(winter.name,end=' --> ')
winter.display_user_balance()

