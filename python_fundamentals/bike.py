class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
    	print("price-"+self.price+"\nspeed-"+self.max_speed+"\nmiles-"+str(self.miles))
    	return self
    def ride(self):
    	self.miles = self.miles+10
    	print("Riding"+str(self.miles))
    	return self
    def reverse(self):
    	self.miles=-5
    	print("Reverse"+str(self.miles))
    	return self
bike1 = Bike("200", "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.displayInfo()

bike2 = Bike("400", "45mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike("300", "65mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()



