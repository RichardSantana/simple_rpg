## A simple RPG game by Richard Santana ##

## The game's characters ##

from characters import Player, Enemy
import time

def play():
    print("------------ Welcome to Simple RPG ------------")

    time.sleep(3)

    print("Please enter your character name: ")

    Player.name = input()

    print(Player.name)

if __name__ == '__main__':
    play()
