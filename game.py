## A simple RPG game by Richard Santana ##

## The game's characters ##

from characters import Player, Enemy
import time

def encounter(player):

    enemy = Enemy(5, 20)

    print("You've encountered an enemy!")

    while enemy.health > 0:
        print("What would you like to do?\nAttack\nRun")
        if input() == "attack":
            enemy.health = enemy.health - player.attack()
        elif input() == "run":
            player.run()
        else:
            print("Invalid response. What would you like to do?\nAttack\nRun")

    print("You win!")

def play():
    print("------------ Welcome to Simple RPG ------------")

    time.sleep(3)

    print("Please enter your character name: ")

    player = Player(input(), 1, 20, 0)

    while(True):
        encounter(player)
    #
    # print(player.name)
    #
    # player.attack()

if __name__ == '__main__':
    play()
