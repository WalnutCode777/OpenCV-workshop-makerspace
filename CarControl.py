class Car:

    def turnOn(self):
        print("Start engine")
        return self

    def turnOff(self):
        print("Off engine")
        return self

    def brake(self):
        print("Brake")
        return self

    def drive(self):
        print("Drive")
        return self

car1 = Car()
car2 = Car()
car3 = Car()

car2.turnOn()

car1.turnOn().drive().brake().turnOff()

car3.turnOn()\
    .drive()\
    .brake()\
    .turnOff()