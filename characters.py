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
        multiplier = random.uniform(5,10) + (self.exp / 100)
        health = int(self.power * multiplier)
        print (f"\n{self.name} heals himself for {health} health!")
        return health

class Enemy(Creature):
    def __init__(self, name, power, health, exp):
        super().__init__(name, power, health, exp)


        tttttttttt3

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
