class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price: ${}".format(self.price))
        print("Speed: {}mph".format(self.speed))
        print("Fuel: {}".format(self.fuel))
        print("Mileage: {}mpg".format(self.mileage))
        print("Tax: {}".format(self.tax*100))
        return self

print("Car 1")
car1 = Car(2000, 35, 'Full', 15)
print("Car 2")
car2 = Car(2000, 5, 'Not Full', 105)
print("Car 3")
car3 = Car(2000, 15, 'Kind of Full', 95)
print("Car 4")
car4 = Car(2000, 25, 'Full', 25)
print("Car 5")
car5 = Car(2000, 45, 'Empty', 25)
print("Car 6")
car6 = Car(20000000, 35, 'Empty', 15)