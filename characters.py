## A simple RPG game by Richard Santana ##

## The game's characters ##

import random

class Player:
    def __init__(self, name, power, health, exp):
        self.name = name
        self.power = power
        self.health = health
        self.exp = exp

    def attack(self):
        multiplier = 10 * random.random()
        damage = self.power * multiplier
        print (f"{self.name} deals {damage} damage!")
        return damage

class Enemy:
    def __init__(self, power, health):
        self.power = power
        self.health = health

# class Imp(Enemy):
#
#     #
#
#
# class Elf(Enemy):
#
#     #
#
#
# class Orc(Enemy):
#
#     #
#
#
# class Dragon(Enemy):
#
#     #
