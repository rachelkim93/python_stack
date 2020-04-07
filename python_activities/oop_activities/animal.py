class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print("Name: {}".format(self.name))
        print("Health: {}hp".format(self.health))

print("Animal 1")
animal1 = Animal("Pangolin", 50)
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, 150)
        # self.health = 150

    def pet(self):
        self.health += 5
        return self

print("Animal 2")
animal2 = Dog("Fido", 150)
animal2.walk().walk().walk().run().run().pet().displayHealth()


# class Dragon(Animal):
#     def __init__(self, name, health):
#         super().__init__(name, 170)
    
#     def fly(self):
#         self.health -= 10
    
#     def display_health(self):
#         super(Dragon, self).display_health()
#         print("I am a dragon!")

# print("Animal 3")
# animal3 = Dragon("Flubber", 170)
# dragon = Dragon("dragon", 170)
# dragon.fly().display_health()

# class Dragon(Animal):
#     def __init__(self, name, health=170):
#         self.name = name
#         self.health = health

#     def fly(self):
#         self.health -= 10
#         return self

#     def display_health(self):
#         super().display_health()
#         print("I am a dragon!")

# dragon = Dragon('dragon')
# dragon.fly().display_health()

print("Animal 4")
animal4 = Animal("Random", 50)
animal4.walk().pet().fly().run().run().displayHealth()


print("Animal 5")
animal5 = Dog("Buster", 50)
animal5.walk().pet().fly()