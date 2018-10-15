#Print 0-150
for num in range(0,151):
	print("Number-",num)


#Print all the multiples of 5 from 5 to 1,000,000
for num in range(5,1000001):
	if(num%5==0):
		print("Number",num)


# Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for num in range(1,101):
	if(num%5==0 and num%10==0):
		print("Coding Dojo")
	elif(num%5==0):
		print("Coding")

#Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for num in range(0,500000):
	if(num%2!=0):
		sum=sum+num
print(sum)

#Print positive numbers starting at 2018, counting down by fours (exclude 0).
for num in range(2018,0,-4):
	print("Number",num)
	

#Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
num = (2,9,3)
for i in range(1,num[1]):
	i=i*num[2]
	if(i>num[0] and i<=num[1]):
		print(i)
	elif(i>num[1]):
		break







