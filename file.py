
# #? Part 1 - Update Values in Dictionaries and Lists

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

#changing 10 to 15 
x[1][0] = 15 
print(x)
print('=================================\n')



#change the last name of the first student L3 from Jordan to Bryant
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
print('=================================\n')


#in the sports_directory, change 'messi' to 'andres'
sports_directory ['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])
print(sports_directory['soccer'])
print('=================================\n')


#change the value 20 in z to 30
z[0]['y'] = 30
print(z)
print(z[0]['y'])
print('=================================\n')


#? Part 2 - Iterate through a list of dictionaries: 
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(some_list):
    for i in some_list:
        for key, value in i.items():
            print(i.items())
            print((f"{key} - {value}"))


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
print('=================================\n')

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#? Part 3 - Get Values From a List of Dictionaries 
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(keyName, listName):
    for i in listName: #iterate through each row
        if keyName in i: #if keyname from function call is in the row then...
            print(i[keyName]) #print row keyName based on function call

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print('=================================\n')


#? Part 4 - Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f'{len(val)} {key}')
        print('\n' .join(val))

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
print('=================================\n')



# output:
"""
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""


