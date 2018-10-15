'''
print("hello world!")
x = "hello dojo!"
print(x)
y = 42
print(y)

x = "hello"*50
print(x)

list = [3,5,1,2]
for i in list:
    print(i)

list = [3,5,1,2]
for i in range(list):
    print(i)

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
def a():
    print(5)
x = a()
print(x)   


x=[]
x=[[5,2,3],[10,8,9]]
for index in range(len(x)):
	for j in range(index):
		if(x[index][j]==10):
			x[index][j]=15
print(x)

class User:
    name="Anna"
anna = User()
print("anna's name:", anna.name)                            
User.name = "Bob"
print("anna's name after change:", anna.name)               
bob = User()
print("bob's name:", bob.name)                              

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    
user1 = User("Anna Propas", "anna@anna.com")
print(user1.name)
print(user1.logged)
print(user1.email)
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
      
print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Attempt 1")
