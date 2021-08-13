#!/usr/bin/python3
import random
import sys
import carddeck
import player
import json
import time
from random import randint
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format



player1 = player.Player()

dungeondeck = carddeck.dungeoncard
dungeonname = ["curse", "bonus", "side kick", "class", "wandering"]
treasuredeck = carddeck.treasurecard
random.shuffle(dungeondeck)
random.shuffle(treasuredeck)

#add dungeon cards to players deck
count = 0
for i, card in enumerate(dungeondeck):
    if count == 3:
        break
    player1.cards.append(card)
    dungeondeck.pop(i)
    count += 1

#add treasure cards to players deck
count = 0
for i, card in enumerate(treasuredeck):
    if count == 2:
        break
    player1.cards.append(card)
    treasuredeck.pop(i)
    count += 1


trashdeck = []


# Print the status of the player
def status():
    print('---------------------------')
    print("Player Level:", player1.level)
    print("Bonus Points:", player1.bonus)
    time.sleep(2)
    print("Cards in Hand:", json.dumps(player1.cards, indent=4))
    print("Cards in Play:", json.dumps(player1.cardsinplay, indent=4))
    print('---------------------------')
    time.sleep(3)


# This is for when the player fights a monster or finds and empty room.
def opendoor():
    length = len(dungeondeck)
    current_card = dungeondeck[randint(0, length-1)]
    drawcard(current_card)

    if current_card["name"] in dungeonname:  # if card is in the list of empty door cards
        print("You found an empty dungeon. This will be added to your hand.")
        player1.cards.append(current_card)
        current_card = ""
        if input("Do you want to play a monster card?: ").strip() == "yes":  # since door is empty you can play a monster card
            resp = input("which card?")
            for i in range(len(player1.cards)):
                if player1.cards[i]['name'] == resp:
                    playmonster(player1.cards[i])
                    del player1.cards[i]
                    break
        else:
            return
    if current_card == "":
        return
    if current_card.get("level") <= (player1.level + player1.bonus):
        print("You beat the monster!")
        player1.level += 1
        for i in range(current_card.get("treasure")-1):
            player1.cards.append(treasuredeck[i])
            treasuredeck.pop(i)

    elif current_card.get("level") >= (player1.level + player1.bonus):
        print("OH NO! The monster is to strong.")
        resp = input("Do you want to run away?: ").strip()
        if resp == "yes":
            diceroll = randint(1, 6)
            print("You rolled:", diceroll)
            time.sleep(2)
            if diceroll == 5 or diceroll == 6:
                print("You escaped!")
                status(2)
            else:
                if current_card.get("bad stuff") == "death":
                    print("You died!")
                    player1.level = 1
                    player1.bonus = 0
                    player1.cardsinplay = []
                    trashdeck.insert(0, current_card)
                    status()
                    time.sleep(2)
                elif current_card.get("bad stuff") == "lose a level":
                    player1.level -= 1

        elif current_card.get("bad stuff") == "death":
            player1.level = 1
            player1.bonus = 0
            player1.cardsinplay = []
            trashdeck.insert(0, current_card)
        elif current_card.get("bad stuff") == "lose a level":
            player1.level -= 1


# shows the card drawn for the deck
def drawcard(drawncard):
    print('---------------------------')
    print("Name:", drawncard.get("name"))
    print("Level:", drawncard.get("level"))
    print("Description:", drawncard.get("description"))
    print("Bad Stuff:", drawncard.get("bad stuff"))
    print('---------------------------')


# equip items from your deck
def equip():

    aswr = input("do you have any cards you want to equip? ")
    if aswr == "yes":
        resp = input("which card? ")
        for i in range(len(player1.cards)):
            if player1.cards[i]["name"] == resp:
                player1.cardsinplay.append(player1.cards[i])
                del player1.cards[i]
                break
        for i, x in enumerate(player1.cardsinplay):
            player1.bonus += player1.cardsinplay[i]["bonus"]

    return


# play monster from your deck
def playmonster(wandering):

    if wandering.get("level") <= (player1.level + player1.bonus):
        print("You beat the monster!")
        player1.level += 1
        for i in range(wandering.get("treasure")-1):
            player1.cards.append(treasuredeck[i])
            treasuredeck.pop(i)

    elif wandering.get("level") >= (player1.level + player1.bonus):
        print("OH NO! The monster is to strong.")
        resp = input("Do you want to run away?: ").strip()
        if resp == "yes":
            diceroll = randint(1, 6)
            print(diceroll)
            time.sleep(2)
            if diceroll == 5 or diceroll == 6:
                print("You escaped!")
            else:
                if wandering.get("bad stuff") == "death":
                    print("You died!")
                    time.sleep(2)
                    player1.level = 1
                    player1.bonus = 0
                    player1.cardsinplay = []
                    trashdeck.insert(0, wandering)
                    status()
                elif wandering.get("bad stuff") == "lose a level":

                    player1.level -= 1

        elif wandering.get("bad stuff") == "death":
            player1.level = 1
            player1.bonus = 0
            player1.cardsinplay = []
            trashdeck.insert(0, wandering)
        elif wandering.get("bad stuff") == "lose a level":
            player1.level -= 1


# main
def main():

    cprint(figlet_format('Munchkin', font='starwars'),
           'blue', 'on_white', attrs=['bold'])
    print("Game Rules:")
    print("You can equip treasure card for bonus points")
    print("You open dungeon doors to find a random monster or item")
    print("If you can't beat the monster the bad stuff happens")
    print("When player reaches level 10 you won the game")
    time.sleep(8)
    while True:
        status()
        equip()
        opendoor()
        if player1.level == 10:
            print("You won the game!")
            break


if __name__ == "__main__":
    main()