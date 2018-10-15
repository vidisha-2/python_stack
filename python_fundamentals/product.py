class Product:
    def __init__(self, price, itemname, weight, brand):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.status = "For sale"

    def Sell(self):
        self.status = "To Sold"
        return self
        
    def Tax(self, tax):
    	self.price = price + price*tax
        return self

    def ReturnItem(reason_for_return):
        if(reason_for_return=='defective'):
        	self.status	= 'defective'
        	self.price = 0
        else if(reason_for_return=='like_new'):
       		self.status = "For sale"
       	else if(reason_for_return=='opened'):
        	self.status = 'Used'
        	self.price = price - .2*price
        return self
    def Display_info(self):
    	print("Price-"+self.price+"\nItem-Name "+self.itemname+"\nWeight-"+self.weight+"\nBrand"+self.brand+"\nTax"+str(self.tax)+"\nSell-"+self.status)
    	return self

desk=Product(25, chair, 4, xyz)
desk.Display_info