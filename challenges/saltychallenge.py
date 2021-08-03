#!/usr/bin/env python3
import random

icecream= ["flavors", "salty"] 

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

# Append the integer (not string!) 99 to the list icecream.

icecream.append(99)

input_number = input("Enter a number between 0 and 19:")

print(icecream[2], icecream[0] +", and",tlgclass[int(input_number)],"chooses to be",icecream[1] +".")


# Plus Challenge
rand = random.randint(0, 18)

print(icecream[2], icecream[0] +", and",tlgclass[rand],"chooses to be",icecream[1] +".")
