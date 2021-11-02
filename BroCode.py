# ---------------------------------------
# variable = a container for a value. Behaves as the value that it contains

# #string = a series of characters
# first_name = "Bro"
# last_name = "Code"
# full_name = first_name +" "+ last_name
# print("Hello "+full_name)
# # print(type(first_name))
#
# #int = a whole integer
# age = 21
# age += 1
# print("Your age is: "+str(age))
# # print(type(age))
#
# #float = a decimal number
# height = 250.5
# print("Your height is: "+str(height)+"cm")
# # print(type(height))
#
# #boolean = True or False
# human = True
# print("Are you a human: "+str(human))
# print(type(human))

# ---------------------------------------
# multiple assignment = allows us to assign multiple variables at the same time in one line of code

# name = "Bro"
# age = 21
# attractive = True
#
# name, age, attractive = "Bro", 21, True
#
# print(name)
# print(age)
# print(attractive)
#
# # Spongebob = 30
# # Patrick = 30
# # Sandy = 30
# # Squidward = 30
#
# # Spongebob = Patrick = Sandy = Squidward = 30
#
# # print(Spongebob)
# # print(Patrick)
# # print(Sandy)
# # print(Squidward)

# ---------------------------------------
# string methods
# name = "Bro code"

# print(len(name))
# print(name.find("r"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","s"))
# print(name*3)

# ---------------------------------------
# type cast

# x = 1    # int
# y = 2.0  # float
# z = "3"  # str
# w = True # Bool
# y = int(y)
# z = int(z)
# x = float(x)
# w = str(w)
#
# print(x)
# print(y)
# print(z*3)
# print(w*2)

# ---------------------------------------
# user input

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input(("How tall are you?: ")))
# age = age + 1
# print("Hello " +name)
# print("You are " +str(age)+" years old")
# print("you are " +str(height)+"cm tall")


# ---------------------------------------
# math functions

# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))


# ---------------------------------------
# string slicing

#            indexing[] or slice()
#            [start:stop:step]

# name = "Bro Code"
#
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

#
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])


# ---------------------------------------
# if statements

# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are centery old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# ---------------------------------------
# logical operators (and, or, not)

# temp = int(input("what is the tempeture outside?: "))
#
# if not(temp >= 0 and temp <= 30):
#     print("the temperature is bad today!")
#     print("stay inside!")
#
# elif not(temp < 0 or temp > 30):
#     print("the temperture is good today!")
#     print("go outside!")


# ---------------------------------------
# while loops


# while 1==1:
#     print("Help! I'm stuck in a loop! ")

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Help!" + name)

# ----------------------------------------------
# for loop
#   wile loop = unlimited
#   for loop = limited

# for i in range(10+1):
#     print(i+1)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# ----------------------------------------------
# nested loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# ----------------------------------------------
# loop Control Statements

# break
# continue
# pass

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# ----------------------------------------------
# list

# food = ["pizza", "hamburger", "hotdog", "spaghetti"]
#
# food[0] = "sushi"
#
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()


# print(food[0])

# for x in food:
#     print(x)


# ----------------------------------------------
# 2D list

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[0][0])


# ----------------------------------------------
# tuple = unchangeable

# student = ("Bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
# if "Bro" in student:
#     print("Bro is here!")


# ----------------------------------------------
# set

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# for x in utensils:
#     print(x)

# ----------------------------------------------
# dictionary

# capitals = {'USA':'Wasington DC', 'India':'New Dehli', 'China':'Baijing', 'Russia':'Moscow'}
#
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
#  capitals.clear()
#
#  print(capitals['Russia'])
#  print(capitals['Germany'])
#  print(capitals.get('Germany'))
#  print(capitals.keys())
#  print(capitals.values())
#  print(capitals.items())
#
# for key, value in  capitals.items():
#     print(key, value)

# ----------------------------------------------
# index operator

# name = "bro Code!"
# # if(name[0].islower()):
# #     name = name.capitalize()
#
# # print(name)
#
# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)


# ----------------------------------------------
# function

# def hello(first_name, last_name, age):
#     print("Hello!" + first_name +" "+last_name)
#     print("You are "+ str(age)+" Years old")
#     print("Have a nice day!")
#
# # hello()
# # hello()
# # hello("Bro")
# # my_name = "Bro"
# # hello(my_name)
#
# hello("Bro", "Code", 21)

# ----------------------------------------------
# return statemant

# def multiply(num1,num2):
# #    result = num1 * num2
# #    return result
#     return num1 * num2
# # print(multiply(6,8))
# x = multiply(6,8)
# print(x)

# ----------------------------------------------
# keyword arguments

# def hello(first, middle, last):
#     print("Hello "+first+" "+middle+" "+last)
#
# #hello("Bro", "Dude", "Code")
# hello(last="Bro",middle="Dude",first="Code")


# ----------------------------------------------
# nested functions calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# ----------------------------------------------
# scope
# L = local
# E = Enclosing
# G = Global
# B = Build-in

# name = "Bro" # global scope
# def display_name():
#    # name = "Code" # local scope
#     print(name)
# display_name()
# print(name)

# ----------------------------------------------
# *args

# def add(num1,num2):
#     sum = num1 + num2
#     return sum

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3,4,5,6))

# ----------------------------------------------
# **kwargs
#
# def hello(**kwargs):
# #    print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello",end=" ")
#     for key, value in kwargs.items():
#         print(value,end=" ")
# hello(title="Mr.",first="Bro",middle="Dude",last="Code")

# ----------------------------------------------
# str.format()

# animal = "cow"
# item = "moon"

# print("the "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over {1} the {0}".format(animal, item))
# print("The {nam2} jumped {nam2} over the {nam1}".format(nam2="cow", nam1="moon"))

# text = "the {} jumped over the {}"
# print(text.format(animal, item))

name = "Bro"
print("Hello, my name is {}".format(name))
print("Barev aper")
x = 3