array=[6,5,3,8,1,7,2,4]

def bubblesort(array):
	print("old array",array)
	for i in range(len(array)-1):
		for j in range(len(array)-1-i):
			#print("comparing",array[i],array[i+1])
			if(array[j]>array[j+1]):
				array[j], array[j+1]=array[j+1],array[j]
				#print("swapped",array[i],array[i+1])
			else:
				print("no need to swapp", array[j],array[j+1])
	print("new array",array)
bubblesort(array)