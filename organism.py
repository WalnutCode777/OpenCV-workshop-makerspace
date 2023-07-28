# Multilevel inheritence
class Organism:
    mammal = True

class Animal(Organism):
    alive = True
    wild = False
    name = None

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(str(self.name) + " is eating now")

    def sleep(self):
        print(str(self.name) + " is sleeping now")

class Prey:
    def flee(self):
        print("Flees successfully")

class Predator:
    def hunt(self):
        print("Hunts successfully")

# Child class inherits from parent class
class Rabbit(Animal, Prey):
    def hop(self):
        print(self.name + " is Hopping")

class Hawk(Animal, Predator):
    def fly(self):
        print(self.name + " is Flying")





