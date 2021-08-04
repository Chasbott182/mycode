#!/usr/bin/env python3
import random

alchemistnames = { # Dictionary of alchemy subjects and their acronyms
"earth":
  {"names": ["soil",
            "topsoil",
            "loam",
            "clay",
            "silt",
            "dirt",
            "sod",
            "clod",
            "turf",
            "ground",
            "terrain"]  },

"fire":
  {"names": ["blaze",
            "conflagration",
            "inferno",
            "holocaust",
            "firestorm",
            "flame",
            "burning",
            "combustion"]
  },

"wind":
  {"names": ["breeze",
            "air",
            "gale",
            "hurricane",
            "draft",
            "blow",
            "zephyr",
            "tornado",
            "gust"]
            },

"water":
  {"names": ["sea",
            "ocean",
            "lake",
            "loch",
            "pond",
            "pool",
            "reservoir",
            "river"]
  },

"metal":
  {"names": ["iron", 
            "gold", 
            "silver", 
            "copper", 
            "aluminum", 
            "alloy", 
            "brass", 
            "steel"]
  },

"technology":
  {"names": ["computer", 
            "A.I", 
            "circuit", 
            "processing", 
            "megabyte", 
            "kilabyte", 
            "gigabyte" ]
  },

"health":
  {"names": ["physical",
            "healthiness",
            "fitness",
            "haleness",
            "strength",
            "vigor",
            "soundness",
            "salubrity",
            "life"]
  },

"everything":
  {"names": ["full"]
  }
}

fullalchemist = { # Dictionary of the alchemy subject names
    "name": ["earth", "fire", "wind", "water", "metal", "technology", "health"]
}

print('Welcome to the military we going to assign you your State Alchemist code name.') # Message greeting


message = ""
response = ""
while response == "" or response not in alchemistnames.keys(): # checks if your first reponse is blank
    response = input(f"What do you specialize in {list(alchemistnames.keys())}? ").strip().lower()
    response2 = input("What else do you specialize in? You can leave blank if nothing. ").strip().lower()
    if response == "exit" or response2 == "exit": # Allows for you to exit during the response
        exit()



# if input value from repsonse
if response == "earth":
    earthname = alchemistnames["earth"]["names"]
    message = message + random.choice(earthname)
elif response == "fire":
    firehname = alchemistnames["fire"]["names"]
    message = message + random.choice(firehname)
elif response == "wind":
    windhname = alchemistnames["wind"]["names"]
    message = message + random.choice(windhname)
elif response == "water":
    watername = alchemistnames["water"]["names"]
    message = message + random.choice(watername)
elif response == "metal":
    metalname = alchemistnames["metal"]["names"]
    message = message + random.choice(metalname)
elif response == "technology":
    techname = alchemistnames["technology"]["names"]
    message = message + random.choice(techname)
elif response == "health":
    healthname = alchemistnames["health"]["names"]
    message = message + random.choice(healthname)
elif response == "everything":
    name = alchemistnames["everything"]["names"][0]
    message =  name

while message == "full" and response2 == "": # If reponse is full you can't have response2 blank
    response2 = input(f"You aren't that smart narrow it down. \n {fullalchemist['name']} ").strip().lower()
    if response2 in fullalchemist["name"]:
        message = message + response2      
        print("\nYou are\n")
        print("The",message.capitalize(),"Alchemist")
        exit()
    
if response2 in fullalchemist["name"]: # if response2 is a category add the category to the message
        message = message + response2    
        print("\nYou are\n")
        print("The",message.capitalize(),"Alchemist")
        exit()

# if input value from response2
if response2 == "earth":
    earthname = alchemistnames["earth"]["names"]
    message = message + random.choice(earthname)
elif response2 == "fire":
    firename = alchemistnames["fire"]["names"]
    message = message + random.choice(firename)
elif response2 == "wind":
    windhname = alchemistnames["wind"]["names"]
    message = message + random.choice(windhname)
elif response2 == "water":
    watername = alchemistnames["water"]["names"]
    message = message + random.choice(watername)
elif response2 == "metal":
    metalname = alchemistnames["metal"]["names"]
    message = message + random.choice(metalname)
elif response2 == "technology":
    techname = alchemistnames["technology"]["names"]
    message = message + random.choice(techname)
elif response2 == "health":
    healthname = alchemistnames["health"]["names"]
    message = message + random.choice(healthname)
else:
        print("You chose one option here is your code name.")


print("\nYou are\n")
print("The",message.capitalize(),"Alchemist")

