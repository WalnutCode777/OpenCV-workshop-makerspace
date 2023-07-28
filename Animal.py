# Inheritence
# Parent class
class Animal:
    alive = True
    wild = False
    name = None

    def __init__(self, name):
        self.name = name

    # def __init__(self):
    #     pass

    def eat(self):
        print(str(self.name) + " is eating now")

    def sleep(self):
        print(str(self.name) + " is sleeping now")


# Child class inherits from parent class
class Rabbit(Animal):
    # pass
    def hop(self):
        print(self.name + " is Hopping")

class Cat(Animal):
    # pass
    def run(self):
        print(self.name + " is Running")

class Dolphin(Animal):
    # pass
    def swim(self):
        print(self.name + " is Swimming")

rabbit = Rabbit("Rabbit")
cat = Cat("Cat")
dolphin = Dolphin("Dolphin")

print(rabbit.alive)
cat.eat()
dolphin.sleep()

# rabbit2 = Rabbit()
# cat2 = Cat()
# dolphin2 = Dolphin()
#
# print(rabbit2.alive)
# cat2.eat()
# dolphin2.sleep()

rabbit.hop()
cat.run()

