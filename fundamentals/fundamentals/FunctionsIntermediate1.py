#1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#   1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
#   2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
#   3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
#   4. Change the value 20 in z to 30
z[0]['y']=30

#2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in some_list:
        printStatement = ""
        for k,v in i.items():
            printStatement += k+' - '+v
            if k == 'first_name':
                printStatement += ', '
        print(printStatement)

iterateDictionary(students)
print('----------')

#3 Get Values From a List of Dictionaries
"""
This function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, and then prints the associated 
values within each key's list
"""
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for k,v in i.items():
            if k == key_name:
                print(v)

iterateDictionary2('first_name', students)
print('----------')
iterateDictionary2('last_name', students)
print('----------')


#4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for k,v in dojo.items():
        print(len(v), k)
        for i in v:
            print(i)
        print('----------')
printInfo(dojo)
