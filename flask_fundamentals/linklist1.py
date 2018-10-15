class SLNode:
	def __init__(self,value):
		self.value = value
		self.next = None
	
class SList:
	def __init__(self):
		#node = SLNode(value)
		#self.head = node
		self.head = None

	def addNode(self,value):
		node = SLNode(value)
		#runner = self.head		#when Head has value
		runner = self.head
		runner = node
		while(runner.next!=None):	#check what runner's next is pointing to
			runner = runner.next	# set runner point to runner(new node's: which we set on the line just above) next
		runner.next = node

	def printNode(self):
		runner = self.head
		print("\n\nhead points to ", id(self.head))
		while(runner.next!=None):
			print(runner.value)
			runner = runner.next
		print(runner.value)
		
	def removfromFront(self):
		temp = self.head
		self.head.next = temp
		print(temp.next)
		#self.head = temp.next

print("\n\n\n\n================== StArT OF ThE PrOgRaM ================")

list = SList()
list.addNode(7)
list.addNode(10)
list.addNode("Alice")
list.printNode()
list.removeNode()
list.printNode()



