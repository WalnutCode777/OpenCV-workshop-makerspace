# String data type
import math

# first_name = "Stephen"
# last_name = "Hawking"
# full_name = first_name + " " + last_name
# print(type(first_name))
# # Error checking only happens after execution, will not check back the variable data type or value
# # last_name += 1
# print(type(last_name))
# print(full_name + ", how are you")

# # Integer data type
# age = 21
# age += 1

# last_name = 5
# last_name += 1
# print(age)
# print(last_name)

# print(type(age))
# # print("Your age is: " + age)
# print("Your age is: " + str(age) + "\n")

# # Float data type, approximately 15 decimal digits,
# # but not all decimal values can be represented exactly in binary
# # Python does not have in-built double data type
# weight = 50.0
# print(weight)
# print(type(weight))
# print("Your weight is: " + str(weight) + "kg")
#
# # Boolean data type
# # Looks similar with string, but useful when doing flag checking
# human = False
# # human = "String"
# print(type(human))
# print(human)
# print("Are you a human: " + str(human))

# # multiple assignments, assign multiple variables at the same time in one line
# # Case 1:
# singer_name = "Aimer"
# age = 32
# still_active = True

# singer_name, age, still_active = "Aimer", 32, True
# singer_info = singer_name, age, still_active
# print(singer_info)

# # Case 2:
# # multiple variables with same value, eg: age
# Miko = Suisei = Sora = 22
# print(Miko, Suisei)
# print("\n")
#
# # Useful built-in String methods
# Name = "miko"
# # Name = "12345"
# print(Name)
# print(len(Name))
# # Return the index of the "o"
# print(Name.find("o"))
# print(Name.capitalize())
# print(Name.upper())
# print(Name.lower())
# # Check whether it's a digit in string
# print(Name.isdigit())
# # Check whether all are alphabeticals, return false if there is a space in between
# print(Name.isalpha())
# print(Name.count("o"))
# print(Name.replace("o", "a"))
# print(Name*4)
#
# type casting, converting the data type of a value to another data type
# Generic in python may seem the same as type casting,
# but both are different
# x = 1
# y = 2.0
# z = "3"

# print(int(x))
# print(float(x))
# print(z*4)
# print(int(z)*4)
#
# # Take user input
# nickname = input("What is your name? : ")
# age1 = int(input("How old are you? : "))
# age1 = age1 + 1

# print("Hello " + nickname)
# print("You are " + str(age1) + " years old")
#
# # Math functions
# pi = -3.142
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# # How far is your value from 0
# print(abs(pi))
# print(pow(pi, 4))
# print(math.sqrt(420))
# print(max(x, y, z, pi))
#
# # String slicing, for creating substring by extracting elements from another string
# name2 = "Tokoyami Towa"
# # starting index is inclusive, stopping index is exclusive, spaces doesnt count
# slice_name = name2[0:9]
# slice_name2 = name2[:9]  # Same as previous code
# slice_Lastname = name2[9:14]
# funky_name = name2[0:13:3]
# funky_name2 = name2[::3]  # Can be written like this
# reversed_name = name2[::-2]  # Print from backwards

# print(slice_name)
# print(slice_Lastname)
# print(funky_name)
# print(reversed_name)
#
# # part 2 of string slicing
# # slice object
# website1 = "http://google.com"
# # Since we only want the name of the website, the constant will be http://
# # and .com, so we use starting as 7 which is length of http:// and -4, length of .com
# # This is a slice object, which can be reused
# slice1 = slice(7, -4)

# website2 = "http://facebook.com"
# website3 = "http://wikipedia.com"

# print(website1[slice1])
# print(website2[slice1])
# print(website3[slice1])

# # if statement, aka guard clause, execute if the condition is met
# check_door = str(input("Is the door open?: "))
# if check_door == "Yes":
#     print("Pls close the door")
# else:
#     print("Welcome!")

# check_door = str(input("Is the door open?: "))
# if check_door == "Yes":
#     print("Pls close the door")
# elif check_door == "No":
#     print("Welcome home!")
# else:
#     print("Welcome!")

# flag = []
# # if flag is True:
# #     print("The machine is running")
# # elif flag is False:
# #     print("The machine is off")
# # Difference between
# if flag:
#     print("This variable stores a truthy/valid value")
# else:
#     print("The variable is empty")
#
# # Logical operators
# temp = int(input("What is the temperature?: "))

# if temp >= 25 and temp <= 30:
#     print("The temperature is normal today!")
#     print("Let's play outside!")
# elif temp < 0 or temp > 30:
#     print("The temperature is abnormal today!")
#     print("Stay at home is a wise choice!")

# temp1 = int(input("What is the temperature?: "))
# if not (temp1 >= 25 and temp1 <= 30):
#     print("The temperature is normal today!")
#     print("Let's play outside!")
# elif not (temp1 < 0 or temp1 > 30):
#     print("The temperature is abnormal today!")
#     print("Stay at home is a wise choice!")

# while loop, a loop that will execute as long as the condition is met
# while 1 == 1:
#     print("This will stuck in a loop")

# name3 = None  # Null in python
# while not name3:
#     name3 = input("Enter your name: ")

# print("Welcome home, " + name3)

# # for loop, a loop that will execute limited amount of times
import time

# for i in range(10):
#     print(i)

# for i in range(50, 100+1, 2):
#     print(i)

# name4 = "Gawr Gura"
# for i in name4:
#     print(i)
#
# # Count down timer
# for seconds in range(10, -1, -1):
#     print(seconds)
#     time.sleep(1)

# print("Happy New Year!")

# # Nested loops, the inner loop will finish all of the iterations before finishing
# # one iteration of the "outer loop"

# rows = int(input("Number of rows: "))
# columns = int(input("Number of columns: "))
# symbol = input("Enter a symbol to plot the matrix: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="") # This prevent the cursor from moving down to next line
#     print()

# # Loop control statements,
# # break, continue, pass
# # break = terminate loop entirely
# # continue = skips to next iteration of the loop
# # pass = does nothing, acts as placeholder
# while True:
#     name5 = input("Enter your name: ")
#     if name5 != "":
#         break

# phoneNum = "123-456-789-0"
# phoneNum1 = "123-456-789-0"

# for i in phoneNum:
#     for j in phoneNum1:
#         if i == "-":
#             continue
#         print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# # List, store multiple items in a single variable
# food = ["nasi lemak", "pizza", "hotdog", "spaghetti"]

# print(food)
# food[0] = "unagi don"
# food.append("ice cream")  # append the element to the end of the list
# food.remove("pizza")  # remove the element from the list
# # food.pop()  # remove the last element in the list
# food.insert(0, "sushi")
# # food.sort()
# # food.clear()
# print(food)
# for x in food:
#     print(x)

# # 2D list, a list of lists, multi-list
# drinks = ["coffee", "tea", "coke"]
# dinner = ["nasi lemak", "hotdog", "spaghetti"]
# dessert = ["souffle", "cake", "ice cream"]

# food1 = [drinks, dinner, dessert]

# food2 = [
#     ["coffee", "tea", "coke"],
#     ["nasi lemak", "hotdog", "spaghetti"],
#     ["souffle", "cake", "ice cream"]
# ]
# print(food1)
# print(food1[0])
# print(food1[0][1])

# # Tuple, collection which is ordered and unchangeable,
# # often used to group related data tgt
# singer = ("Aimer", 32, "Deep Down", "Deep", "Deep")

# print(singer.count("Deep"))
# print(singer.index(32))
# print(singer.index("Deep Down"))

# for x in singer:
#     print(x)

# if "Aimer" in singer:
#     print("Name saved!")

# # Set, collection which is unordered, unindexed. Dont allow duplicate values
# cutlery = {"fork", "spoon", "knife", "knife"}
# dishes = {"plate", "cup", "bowl", "knife"}

# cutlery.add("napkin")
# cutlery.remove("spoon")
# cutlery.clear()
# dishes.update(cutlery)
# dinning_table = cutlery.union(dishes)
# # Everytime it prints, the order of elements displayed is different from the
# # previous one, so, it is faster than a list
# for x in cutlery:
#     print(x)

# for x in dinning_table:
#     print(x)

# print(cutlery.difference(dishes))
# print(dishes.difference(cutlery))

# print(cutlery.intersection(dishes))

# # Dictionary, a changeable, unordered collection of unique key:value pairs
# # it is hashtable in Java, so it is very fast to access a value

# country = {"Malaysia": "Kuala Lumpur",
#            "Singapore": "Singapore",
#            "Japan": "Tokyo",
#            "USA": "Washington DC"}

# print(country["Malaysia"])
# # This will have error as it is not in the list, hence, interrupting the program flow
# # print(country["France"])
# # Better way to check if the element is in the list
# print(country.get("France"))
# print(country.keys())
# print(country.values())
# print(country.items())
# # Alternative way to print key:value pairs
# for k, v in country.items():
#     print(k, v)

# country.update({"Germany": "Berlin"})
# country.update({"Japan": "Osaka"})
# country.pop("Malaysia")
# # country.clear()
# for key, value in country.items():
#     print(key, value)

# # Function, a block of code which is executed when it is called


# def whoAreYou(firstName: str, lastName: str, age: int, hobby: str):
#     print("Hi " + firstName, lastName)
#     print("I am " + str(age))
#     print("I love " + hobby)


# whoAreYou("Leong", "Tze Heng", "22", "programming")
# # Key arguments, order of arguments dont matter
# whoAreYou(lastName="Tze Heng", age=22, hobby="programming", firstName="Leong")

# # return function, function sends Python values/objects back to the caller
# # these values are called return values


# def multiply(number1, number2):
#     result = number1 * number2
#     return result


# print(float(multiply(5, 2)))
# # Nested function
# print(round(abs(float(input("Enter a number: ")))))

# Random
# import random

# x = random.randint(1, 100)
# y = random.random()  # random float number
# print(x, y)

# game = ['rock', 'paper', 'scissors']
# z = random.choice(game)
# print(z)

# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

# random.shuffle(cards)
# print(cards)

# # OOP in python
# # OOP means we want to create reusable code, like a toolkit
from selfDrivingCar import Car

car1 = Car("Tesla", "model S", 2012, "red")
car2 = Car("Ford", "Mustang", 2022, "blue")

# print(car1.model)
# print(car2.model)
# car1.drive()
# car1.stop()

# car2.drive()
# car2.stop()

# class variables
car2.wheel = 2
print(car1.wheel)
print(car2.wheel)
# Can be change globally
Car.wheel = 3
print(car1.wheel)
print(car2.wheel)
