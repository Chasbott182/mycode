#!/usr/bin/env python3

hero = {'name': 'Spider-Man', 'real name': 'Peter Parker', 'age': 17, 'powers': ['spidey sense', 'super strength', "mosquito catchin'", 'agility'], 'weaknesses': ['Mary Jane', 'Uncle Ben', 'symbiote']}

print(hero)

# Print real name value
print(hero["real name"])

# Print mosquito catchin'
print(hero["powers"][2])

# Print all weaknesses
print(*hero["weaknesses"])
