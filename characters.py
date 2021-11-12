## A simple RPG game by Richard Santana ##

## The game's characters ##

import random

class Creature:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
        self.exp = exp

    def attack(self):
        multiplier = random.uniform(5,6)
        damage = self.power * multiplier
        print (f"{self.name} deals {damage} damage!\n")
        return damage

class Player(Creature):
    def __init__(self, name, power, health, exp):
        super().__init__(name, power, health)
        self.exp = exp

    def heal():
        multiplier = random.uniform(3,4)
        recovery = self.power * muliplier


class Enemy(Creature):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)

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
