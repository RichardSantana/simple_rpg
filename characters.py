## A simple RPG game by Richard Santana ##

## The game's characters ##

import random

class Creature:
    def __init__(self, name, power, health, exp):
        self.name = name
        self.power = power
        self.health = health
        self.exp = exp

    def attack(self):
        multiplier = random.uniform(4,6) + (self.exp / 100)
        damage = int(self.power * multiplier)
        print (f"\n{self.name} deals {damage} damage!")
        return damage

class Player(Creature):
    def __init__(self, name, power, health, exp):
        super().__init__(name, power, health, exp)

    def heal(self):
        multiplier = random.uniform(7,12) + (self.exp / 100)
        health = int(self.power * multiplier)
        print (f"\n{self.name} heals himself for {health} health!")
        return health

class Enemy(Creature):
    def __init__(self, name, power, health, exp):
        super().__init__(name, power, health, exp)
#
# class Imp(Enemy):
#
#     def __init__(self, name, power, health, exp):
#
# class Elf(Enemy):
#
#     def __init__(self, name, power, health, exp):
#         self.name = "Elf"
#         self.power = 1.25
#         self.health = 40
#         self.exp = 50
#
# class Orc(Enemy):
#
#     def __init__(self, name, power, health, exp):
#         self.name = "Orc"
#         self.power = 1.5
#         self.health = 60
#         self.exp = 100
#
# class Dragon(Enemy):
#
#     def __init__(self, name, power, health, exp):
#         self.name = "Dragon"
#         self.power = 2
#         self.health = 200
#         self.exp = 100000
