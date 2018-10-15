class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.fuel = fuel
        self.speed = speed
        self.mileage = mileage
        if(int(price)>10000):
        	self.tax=0.15
        else:
        	self.tax=0.12

        self.display_all()

    def display_all(self):
    	print("Price-"+self.price+"\nFuel"+self.fuel+"\nSpeed-"+self.speed+"\nMileage"+self.mileage+"\nTax"+str(self.tax))
    	return self


car1 = Car("2000","35mph","Full","15mpg")
car2 = Car("20000","15mph","Not Full","15mpg")
car3 = Car("1000","20mph","Full","15mpg")
car4 = Car("200","15mph","Not Full","15mpg")
car5 = Car("5000","10mph","Not Full","15mpg")
car6 = Car("123000","40mph","Full","15mpg")
car1.display_all()