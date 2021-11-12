## A simple RPG game by Richard Santana ##

## The game's characters ##

import random

class Creature:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        multiplier = 10 * random.random()
        damage = self.power * multiplier
        print (f"{self.name} deals {damage} damage!")
        return damage

class Player(Creature):
    def __init__(self, name, power, health, exp):
        super().__init__(name, power, health)
        self.exp = exp

class Enemy(Creature):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)

#TEST4

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
