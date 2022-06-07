#1
"""
This function accepts a number as an input. 
Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
"""
def Countdown(num):
    numArr = []
    for i in range(num, -1, -1):
        numArr.append(i)
    
    return numArr


#2
"""
This function receive a list with two numbers as input, then Print the first value and return the second.
"""
def PrintAndReturn(numList):
    print(numList[0])
    return numList[1]


#3
"""
This function accepts a list and returns the sum of the first value in the list plus the list's length.
"""
def FirstPlusLength(numArr):
    return numArr[0]+len(numArr)



#4
"""
This function accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
"""
def valuesGreaterThanSecond(numList):
    rtList = []
    for i in numList:
        if i > 2:
            rtList.append(i)
    
    if len(rtList) < 2:
        return False
    else:
        print(rtList[1])
    
    return rtList
print(valuesGreaterThanSecond([3]))

#5
"""
This function accepts two integers as parameters: size and value. 
The function returns a list whose length is equal to the given size, and whose values are all the given value.
"""
def length_and_value(size, value):
    rtList = []
    for i in range(0,size):
        rtList.append(value)
    
    return rtList