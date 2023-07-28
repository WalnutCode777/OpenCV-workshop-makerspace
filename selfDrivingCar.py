class Car:

    # class variable
    wheel = 4 # So by default all car has 4 wheels
    # constructor
    def __init__(self, manufacture, model, year, color):
        # Need to add self. becuz we are preceding each of these attributes
        # with itself, which is the object we are working on
        self.manufacture = manufacture # instace variable
        self.model = model # instace variable
        self.year = year # instace variable
        self.color = color # instace variable

    # self refers to the object that is using this method
    # the variable name of object will replace the self
    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopping")