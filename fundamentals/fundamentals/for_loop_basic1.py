#This function Prints all integers from 0 to 150.
def basic():
    for i in range(151):
        print(i)

# This function Prints all the multiples of 5 from 5 to 1,000
def multiplesOfFive():
    for i in range(5,1001):
        if i%5 ==0:
            print(i)
# This function Prints integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def countingTheDojoWay():
    for i in range(1,101):
        if i%10 ==0:
            print("Coding Dojo")
        elif i%5 ==0:
            print("Coding")
        else:
            print(i)

#This function Adds odd integers from 0 to 500,000, and print the final sum.
def whoaThatSuckerIsHuge():
    sum = 0
    for x in range(0,500001):
        if x%2 !=0:
            sum +=x
    print(sum)

#This function Prints positive numbers starting at 2018, counting down by fours.
def countdownByFours():
    for x in range(2018, 0, -4):
        print(x)
        
#This function provies a flexiable counter, starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
def FlexibleCounter(lowNum, highNum, mult):
    for x in range(lowNum, (highNum+1)):
        if x%mult == 0:
            print(x)