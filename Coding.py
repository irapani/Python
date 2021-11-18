import sys
import math
import random
import threading
import time
from functools import reduce

# data types

print("Random", random.randint(1, 101))
print(math.inf > 0)

print(math.inf - math.inf)

#conditions

age = 30
if age > 21:
    print("you can drive car")
else:
    print("you can ride a bike")

age = 30
if age:
    print("stay home")
elif (age >= 5) and (age <= 6):
    print("goto kindergarden")
elif (age > 6 ) and (age <=17):
    print("Grade", (age - 5))
else:
    print("College")

#String

print(r"I'll be ignored \n")
print("hello" + "You")
str3 = "Hello You"
print("Lenght", len(str3))
print("1st", str3[0])
print("last", str3[-1])

print("1st", str3[0:3])
print("Every other", str3[0:-1:2])

str3 = str3.replace("Hello", "Goodbye")
print(str3)

print("You" not in str3)
print("You index", str3.find("You"))
print("    Hello     ".strip())

print("".join(["Some", "Word"]))
print("A String".split(" "))

int1 = int2 = 5
print(f'{int1} + {int2} = {int1} + {int2}')

print("A String".lower())
print("A String".upper())

print("AString123".isalnum())
print("AString".isalpha())
print("123""".isdigit())

#list are Mutable (can be changed) inMutable (cant be changed)

l1 = [1, 3.14, "Derek", True]

print("Length", len(l1))
print("1st", l1[0])
print("Last", l1[-1])

l1[0] = 2
l1[2:4] = ["Bob", False]
l1[2:2] = ["Paul", 6]
