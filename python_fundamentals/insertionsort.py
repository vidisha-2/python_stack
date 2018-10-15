array=[6,5,3,8,1,7,2,4]

def insertionsort(array):
	for i in range(1,len(array)):
		min_val=array[i]
		#print(min_val)
		#print(array[i-1]>min_val)
		while(i>0 and array[i-1]>min_val):
			array[i]=array[i-1]
			i=i-1
		array[i]=min_val
		
	print(array)
insertionsort(array)


