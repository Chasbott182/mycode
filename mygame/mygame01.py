#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

from player import Player
from monster import Monster

name = input("Please enter players name. ").strip()

player1 = Player(name)


# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      equip sword
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(player1.inventory))
    print('spells : ' + str(player1.inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if "weapon" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['weapon'])
    print("---------------------------")


# an inventory, which is initially empty
# inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
        'weapon': 'sword'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room',

    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            player1.addinventory(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        elif "weapon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['weapon']:
            # add the item to their inventory
            player1.addinventory(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['weapon']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'go' first
    if move[0] == 'equip':
        # check if the they are equipping a sword
        if move[1] in player1.inventory and move[1] == "sword":
            # add a damage bonus to the players attack
            player1.equipweapon(move[1])
        # you can only equip a sword
        else:
            print('You can\'t equip that!')

    if move[0] == 'drink':
        # check if the they have a potion
        if move[1] in player1.inventory and move[1] == "potion":
            # add bonus health to the player
            player1.drink()
        # you can only drink a potion
        else:
            print('You can\'t do that!')

    if move[0] == 'read':
        # check if the they have a book
        if move[1] in player1.inventory and move[1] == "spell book":
            # add a spell to the players list of spells
            player1.addspells("magic missile")
        # you can only equip a sword
        else:
            print('You can\'t do that!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in player1.inventory and 'potion' in player1.inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    if currentRoom == 'Garden' and player1.level > 1:
            print('You defeated a monster and leveled you can escape the house... YOU WIN!')
            break

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("Ahh, a monster has found you fight!")
        print("Type 'attack' to attack.")
        monster = Monster()
        while True:
            print(f"{player1.name}'s Health: {player1.health}, Monsters Health: {monster.health}")

            action = input("Attack! ")

            if action == "attack":
                monster.health += player1.attack()
            elif action == "cast":
                if action[1] in player1.spells:
                    print(f"{player1.name} casts {action[1]}")
                    monster.health += player1.cast()
            else:
                print("You can do that. Your in the middle of combat!")

            print(f"Monster attacks and does {monster.attack} damage!")
            player1.health += monster.attack

            if monster.health <= 0:
                print('YOU KILLED THE MONSTER!')
                print('You gained a level, and a item that the monster dropped.')
                player1.addinventory("spell book")
                player1.level += 1
                del rooms[currentRoom]['item']
                break
            elif player1.health <= 0:
                print('A monster has got you... GAME OVER!')
                exit()

