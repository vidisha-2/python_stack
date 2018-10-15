'''
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
'''
#1How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x=[]
x=[[5,2,3],[10,8,9]]
for index in range(len(x)):
	for j in range(index):
		if(x[index][j]==10):
			x[index][j]=15
print(x)

#2How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
for key in range(len(students)):
	for value in students[key]:
		if(students[key][value]=='Jordan'):
			students[key][value]='Bryant'
print(students)

#For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
'''print(sports_directory['soccer'][0])
for key in range(len(sports_directory)):
														#iterating through key till the length of the list  
	for index in sports_directory[key]: 
		print(sports_directory[key][index])
		if(sports_directory[key][index]=='Messi'):
			sports_directory[key][index]='Andres'

print(sports_directory)'''
for key, val in sports_directory.items():
	# print(val)
	for index in range(len(val)):
		#print(index)
		if(val[index]=='Messi'):
			val[index] ='Andres'
print(sports_directory)


#For z, how would you change the value 20 to 30?
z = [ {'x': 10, 'y': 20} ]
for key in range(len(z)):
	for value in z[key]:
		if(z[key][value]==20):
			z[key][value]=30
print(z)


'''2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and
 the associated value.  For example, given the following list:
 students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
'''
dictt=[{'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def printKeyValue(students):
	for key in students:
		print("first_name-"+key['first_name']+" "+"last_name-"+key['last_name'])

printKeyValue(dictt)


'''3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key 
for each dictionary.  For example, iterateDictionary2('first_name', students) should output
Michael
John
Mark
KB
'''
students=[{'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def printKeyValue(students,skey):
	for index in range(len(students)):
		for key,val in students[index].items():
			if(key==skey):
				print(val)
			
printKeyValue(students,'first_name')



'''

Create a function that prints the name of each location and also how many locations the Dojo currently has. 
Have the function also print the name of each instructor and how many instructors the Dojo currently has.  
For example, printDojoInfo(dojo) should output
'''
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo(dojo):
	for key,value in dojo.items():
		print(f"{len(value)}"+key)
		print(value)
	
printDojoInfo(dojo)

