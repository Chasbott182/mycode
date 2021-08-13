#!/usr/bin/python3
import random
import threading
import carddeck
import player
import json
from random import randint



# while player <= 1:
#     print("You must enter 2 or players to start game.")
#     players = input("How many players do you want?: ")

# for x in range(1, players):
player1 = player.Player()

dungeondeck = carddeck.dungeoncard
dungeonname = ["curse", "bonus", "side kick", "class", "wandering"]
treasuredeck = carddeck.treasurecard
random.shuffle(dungeondeck)
random.shuffle(treasuredeck)

count = 0
for i, card in enumerate(dungeondeck):
    if count == 3:
        break
    player1.cards.append(card)
    dungeondeck.pop(i)
    count += 1

count = 0
for i, card in enumerate(treasuredeck):
    if count == 2:
        break
    player1.cards.append(card)
    treasuredeck.pop(i)
    count += 1


trashdeck = []


def status():
    print('---------------------------')
    print("Player Level:", player1.level)
    print("Bonus Points:", player1.bonus)
    print("Cards in Hand:", json.dumps(player1.cards, indent=4))
    print("Cards in Play:", json.dumps(player1.cardsinplay, indent=4))
    print('---------------------------')


def opendoor():
    length = len(dungeondeck)
    current_card = dungeondeck[randint(0, length-1)]
    drawcard(current_card)

    if current_card["name"] in dungeonname:
        print("You found an empty dungeon. This will be added to your hand.")
        player1.cards.append(current_card)
        current_card = ""
        if input("Do you want to play a monster card?").strip() == "yes":
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
        resp = input("Do you want to run away").strip()
        if resp == "yes":
            diceroll = randint(1, 6)
            print("You rolled:", diceroll)
            if diceroll == 5 or diceroll == 6:
                print("You escaped!")
            else:
                if current_card.get("bad stuff") == "death":
                    print("You died!")
                    player1.level = 1
                    player1.bonus = 0
                    player1.cardsinplay = []
                    trashdeck.insert(0, current_card)
                elif current_card.get("bad stuff") == "lose a level":

                    player1.level -= 1

        elif current_card.get("bad stuff") == "death":
            player1.level = 1
            player1.bonus = 0
            player1.cardsinplay = []
            trashdeck.insert(0, current_card)
        elif current_card.get("bad stuff") == "lose a level":
            player1.level -= 1


def drawcard(drawncard):
    print('---------------------------')
    print("Name:", drawncard.get("name"))
    print("Level:", drawncard.get("level"))
    print("Description:", drawncard.get("description"))
    print("Bad Stuff:", drawncard.get("bad stuff"))
    print('---------------------------')


def equip():

    aswr = input("do you have any cards you want to equip?")
    if aswr == "yes":
        resp = input("which card?")
        for i in range(len(player1.cards)):
            if player1.cards[i]["name"] == resp:
                player1.cardsinplay.append(player1.cards[i])
                del player1.cards[i]
                break
        for i, x in enumerate(player1.cardsinplay):
            player1.bonus += player1.cardsinplay[i]["bonus"]

    return


def playmonster(wandering):

    if wandering.get("level") <= (player1.level + player1.bonus):
        print("You beat the monster!")
        player1.level += 1
        for i in range(wandering.get("treasure")-1):
            player1.cards.append(treasuredeck[i])
            treasuredeck.pop(i)

    elif wandering.get("level") >= (player1.level + player1.bonus):
        print("OH NO! The monster is to strong.")
        resp = input("Do you want to run away").strip()
        if resp == "yes":
            diceroll = randint(1, 6)
            print(diceroll)
            if diceroll == 5 or diceroll == 6:
                print("You escaped!")
            else:
                if wandering.get("bad stuff") == "death":
                    print("You died!")
                    player1.level = 1
                    player1.bonus = 0
                    player1.cardsinplay = []
                    trashdeck.insert(0, wandering)
                elif wandering.get("bad stuff") == "lose a level":

                    player1.level -= 1

        elif wandering.get("bad stuff") == "death":
            player1.level = 1
            player1.bonus = 0
            player1.cardsinplay = []
            trashdeck.insert(0, wandering)
        elif wandering.get("bad stuff") == "lose a level":
            player1.level -= 1


def main():

    while True:
        status()
        equip()
        opendoor()


if __name__ == "__main__":
    main()