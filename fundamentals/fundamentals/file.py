#Variable declaration
num1 = 42 
num2 = 2.3 
boolean = True 
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')

 #log statement
print(type(fruit)) 
print(pizza_toppings[1]) 
pizza_toppings.append('Mushrooms') #adding mushrooms to the toppings list
print(person['name']) 
person['name'] = 'George' # changing the name from John
person['eye_color'] = 'blue' # setting the eye_color
print(fruit[2]) 

# conditionals
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!") 
elif len(string) > 15:
    print("It's a long word!") 
else:
    print("Just right!") 

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # remove the last item from the list (Mushroom)
pizza_toppings.pop(1) # remove the second item from the list (Sausage)

print(person) 
person.pop('eye_color')  # removing the eye_color key-value from dictionary
print(person) 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')  
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') 

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')  

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') 

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)