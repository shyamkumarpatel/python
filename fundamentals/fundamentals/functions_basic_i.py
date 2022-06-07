#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())    # Print the value of function number_of_food_groups, which is 5


#2
def number_of_military_branches():
    return 5
print(#number_of_days_in_a_week_silicon_or_triangle_sides() + #
       number_of_military_branches()) 
""" This above print statement will result in
Error, number_of_days_in_a_week_silicon_or_triangle_sides is expecting 2 aruguments
Commenting out the function call to number_of_days_in_a_week_silicon_or_triangle_sides so that the code will run and return 5
"""

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #This statement will print the returning value of the number_of_books_on_hold, which in this case is 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) # This function will return 5, which will be printed in terminal


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()  # Assign the returning value of function, which is none, into x
print(x) # print the value of variable x


#6
def add(b,c):
   return b+c
print(add(1,2) + add(2,3))


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) # This line print the returning value of concatenate function, which converts the b and c variable into string, add them then return those values


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#The above code snippet call the function number_of_oceans_or_fingers_or_continents (print the value of b, 100) and print that value 10


#9
# This function below return either 7 or 1, depending on the value of the input parameter b and c.
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # print the returning value of 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # print the returning value of 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
 # print the returning value of 7 plus returning value of 14 which would result in 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) # Print 8
# print the returning value of function addition, which return sum of input parameter b and c


#11
b = 500
print(b)     #Print 500
def foobar():
    b = 300
    print(b)
print(b)     #Print 500
foobar()     #Print 300
print(b)     #Print 500


#12
b = 500
print(b)      #Print 500
def foobar():
    b = 300
    print(b)
    return b
print(b)      #Print 500
foobar()      #Print 300
print(b)      #Print 500


#13
b = 500
print(b)      #Print 500
def foobar():
    b = 300
    print(b)
    return b
print(b)      #Print 500
b=foobar()    #Print 300
print(b)      #Print 300


#14
def foo():
    print(1)     #Print 1
    bar()        #Print 3
    print(2)     #Print 2
def bar():
    print(3)
foo()


#15
def foo():
    print(1)      #Print 1
    x = bar()     #Print 3
    print(x)      #Print 5
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)          #Print 10



