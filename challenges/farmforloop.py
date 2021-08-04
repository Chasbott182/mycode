#!/usr/bin/env python3

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats","chickens"]
farm = ["NE Farm", "W Farm", "SE Farm", "E Farm", "W Farm"]

num=0
user=""

for animal in farms[1]["agriculture"]:
    print(animal)
print("\n")

while user == "" or user not in farm:
    user = input("Choose a farm. (NE Farm, W Farm, SE Farm, E Farm, or W Farm)").strip()


for index ,animal in enumerate(farms):
    if user == animal.get("name"):
        num = index
print("\n")


for animal in farms[num]["agriculture"]:
    print(animal)
print("\n")

for animal in farms[num]["agriculture"]:
    if animal in animals:
        print(animal)

    else:
        continue

