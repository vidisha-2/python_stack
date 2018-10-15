class SLNode:
	def __init__(self,value):
		self.value = value
		self.next = None
	
class SList:
	def __init__(self,value):
		node = SLNode(value)
		self.head = node

	def addNode(self,value):
		node = SLNode(value)
		runner = self.head
		while(runner.next!=None):	#check what runner's next is pointing to
			runner = runner.next	# set runner point to runner(new node's: which we set on the line just above) next
		runner.next = node
	
	def addToFront(self,value):
		temp = self.head
		node = SLNode(value)
		node.next = temp
		self.head = node

	def printNode(self):
		runner = self.head
		print("\n\nhead points to ", id(self.head))
		while(runner.next!=None):
			print(runner.value)
			runner = runner.next
		print(runner.value)
		
	def removeFromFront(self):
		runner = self.head					#remove from the front
		runner = runner.next
		self.head = runner
		
	def removeFrommiddle(self,val):
		runner = self.head
		#print("set at",self.head.value)
		runnerF = runner.next
		#print("value at runner.next",runner.value,runner.next)
		while(runnerF.next!=None and runnerF.value!=val):
			#print("i m in",runner.value)
			#print("Value not found")
			runner = runner.next
			runnerF = runnerF.next
		
		prevnode = runner
		prevnode.next = runnerF.next
		#runner = prevnode			
		#runner = runner.next

	def removeFromBack(self):
		runner = self.head
		runnerF = runner.next
		while(runnerF.next!=None):
			runner = runner.next
			runnerF = runnerF.next
		runner.next = None
		#self.head = runner


print("\n\n\n\n================== StArT OF ThE PrOgRaM ================")

list = SList(2)
list.addNode(7)
list.addNode(10)
list.addNode("Alice")
list.addNode(1)
list.addNode(5)
list.addToFront("Einstein")
list.printNode()
list.removeFrommiddle(7)
list.removeFromBack()
list.printNode()
