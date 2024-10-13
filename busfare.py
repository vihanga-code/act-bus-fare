class vehicle:
    def __init__(self,people,old_price):
        self.people=people
        self.old_price=old_price
    def display(self):
        print(self.people*self.old_price)    
class bus (vehicle):
    def __init__(self,people,old_price,new_price):
        self.new_price=new_price
        vehicle.__init__(self,people,old_price)
    def display1 (self):
        print(self.people*self.new_price)
obj=bus(50,100,110) 
obj.display()
obj.display1()
       