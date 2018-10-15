'''
As part of this assignment, please create a function randInt() where

randInt() returns a random integer between 0 to 100
randInt(max=50) returns a random integer between 0 to 50
randInt(min=50) returns a random integer between 50 to 100
randInt(min=50, max=500) returns a random integer between 50 and 500
Create this function without using random.randInt() but you are allowed to use random.random().
'''
import random
def randInt(min=0,max=100):

		print(f"Random integer {min} to {max}",int(random.uniform(min,max)))
		
randInt()
randInt(max=50)
randInt(min=50) 
randInt(min=50, max=500)
