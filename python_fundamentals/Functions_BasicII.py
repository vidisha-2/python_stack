'''Countdown - Create a function that accepts a number as an input. 
Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).
For example countDown(5) should return [5,4,3,2,1,0].
'''
def countdown(x):
	for idx in range(x,-1,-1):
		print(idx)
countdown(5)

'''Print and Return - Your function will receive an array with two numbers.
 Print the first value, and return the second.
 '''
def printAndReturn(x,y):
	print(x)
	return y
b=printAndReturn(2,4)
#print(b)

'''Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that 
are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the 
function return False
'''
def greaterThanSecond(array):
	count=0
	for num in range(len(array)):
		if(len(array)<1):
			print(false)
		elif(len(array)>1):
			check=array[1]
		if(array[num]>check):
			count=count+1
	print(count)
greaterThanSecond([9999,999,111,22])

'''This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value.
This function should take two numbers and return a list of length size containing only the number in value.
For example, lengthAndValue(4,7) should return [7,7,7,7].
'''
def lengthAndValue(size,value):
	list=[]
	for num in range(size):
		list.append(value)
	print(list)
lengthAndValue(4,7)
