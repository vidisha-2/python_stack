array=[6,5,3,8,1,7,2,4]


def selectsort(array):
	for i in range(len(array)-1):
		min_value=i
		print(min_value)
		for j in range(i,len(array)):
			if(array[min_value]>array[j]):
				min_value=j
			
		temp=array[i]
		array[i]=array[min_value]
		array[min_value]=temp
	
	print(array)
selectsort(array)