class Bike(object):
    def __init__(self, price, max_speed): 
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Bike's Price: ${}".format(self.price))
        print("Bike's Maximum Speed: {} mph".format(self.max_speed))
        print("Total Miles Ridden: {} miles".format(self.miles))
        return self

    def ride(self):
        self.miles += 10
        print("Riding", self.miles)
        return self

    def reverse(self): 
        if self.miles < 6:
            print("Cannot reverse")
        else:
            self.miles -= 5
            print("Reversing", self.miles)
        return self

instance1 = Bike(200, 25)
instance2 = Bike(100, 10)
instance3 = Bike(500, 50)

print("Bike 1")
instance1.ride().ride().ride().reverse().displayInfo()
print("Bike 2")
instance2.ride().ride().reverse().reverse().displayInfo()
print("Bike 3")
instance3.reverse().reverse().reverse().displayInfo()
