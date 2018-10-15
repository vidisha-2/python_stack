class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 10
    def walk(self):
    	self.health -= 1
    	return self
    def run(self):
    	self.health += 5
    	return self
    def display_health(self):
    	print("Name-"+self.name+"\nHealth-"+str(self.health))
    	return self

class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super().__init__()
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		super().display_health()
		print("I am a Dragon")
		return self

animal1=Animal("Einstein")
animal1.walk().walk().walk()
animal1.run().run()
animal1.display_health()

c=Dog("Peet")
c.walk().walk().walk()
c.run().run()	
c.pet()
c.display_health()
#c.fly()


animal2=Animal("Darwin")
#animal2.pet()
#animal2.fly()
animal2.display_health()




        