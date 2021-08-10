#!/usr/bin/python3

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.inventory = []
        self.weapon = 0
        self.level = 1
        self.spells = []
    #
    # equipping adds attack damage to players
    def equipweapon(self, item):
        if item != "sword":
            return "You can only equip a weapon."
        else:
            self.weapon = -5
            print("You equipped a sword. Now you can do more damage")

    # This a allows the player to attack and do damage
    def attack(self):
        return -5 + self.weapon

    def drink(self, item):
        self.health += 10
        self.inventory.remove(item)
        print("You just boosted your health by 10!")

    def cast(self):
        return -6

    def addspells(self, item):
        self.spells.append(item)

    def addinventory(self, item):
        self.inventory.append(item)

    def removeitem(self, item):
        self.inventory.pop(item)
