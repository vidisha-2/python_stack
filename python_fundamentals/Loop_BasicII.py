'''Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
'''
def biggieSize(array):
	for num in range(len(array)):
		if(array[num]>0):
			array[num]='big'
	return array
print(biggieSize([-1,3,5,-5]))

'''Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. 
Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it. 
(Note that zero is not considered to be a positive number).
'''
def countPositives(array):
	count=0
	for num in range(len(array)):
		if(array[num]>0):
			count=count+1
	array[len(array)-1]=count
	return array
print(countPositives([-1,1,1,1]))


'''SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  
For example sumTotal([1,2,3,4]) should return 10
'''
def sumTotal(array):
	sum=0
	for num in range(len(array)):
		sum=sum+array[num]
	return sum
print(sumTotal([1,2,3,4]))


'''Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  
or example multiples([1,2,3,4]) should return 2.5
'''
def aveRage(array):
	sum=0
	for num in range(len(array)):
		sum=sum+array[num]
	avg=sum/len(array)
	return avg
print(aveRage([1,2,3,4]))


'''Length - Create a function that takes an array as an argument and returns the length of the array.  
For example length([1,2,3,4]) should return 4
'''
def length_array(array):
	print(array)
	a_len=len(array)
	return a_len
print(length_array([1,2,3,4]))


'''Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  
If the passed array is empty, have the function return false.  
For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3
'''
def minimumArray(array):
	min=array[0]
	for num in range(len(array)):
		if(array[num]<min):
			min=array[num]
	return min
print(minimumArray([-1,-2,-3]))


'''Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  
If the passed array is empty, have the function return false.  
For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
'''
def maximumArray(array):
	max=array[0]
	for num in range(len(array)):
		if(array[num]>max):
			max=array[num]
	return max
print(maximumArray([-1,-2,-3]))


'''UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, 
average, minimum, maximum and length of the array.
'''

def ultimateAnalyze(array):
	max=array[0]
	min=array[0]
	sum=0
	for num in range(len(array)):
		sum = sum + array[num]
		if(array[num]>max):
			max=array[num]
		if(array[num]<min):
			min=array[num]
	ave_rage = sum / len(array)
	len_array = len(array)
	d = dict()
	d['Sum']=sum
	d['Average']=ave_rage
	d['Minimum']=min
	d['Maximum']=max
	d['Length']=len_array
	return d
print(ultimateAnalyze([1,2,3,0]))


'''ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  
Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1].
'''
def reverse(array):
	for num in range(int(len(array)/2)):
		temp=array[num]
		array[num]=array[len(array)-1-num]
		array[len(array)-1-num]=temp
	return array
print(reverse([1,2,3,4]))