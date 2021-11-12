## A simple RPG game by Richard Santana ##

## The game's characters ##

from characters import Player, Enemy
import time

def encounter(player):

    time.sleep(1)

    enemy = Enemy("Imp", 1, 20)

    print("You've encountered an enemy!\n")

    time.sleep(1)

    while enemy.health > 0:
        time.sleep(1)

        print("What would you like to do?\nAttack\nHeal\nRun\n")

        if input() == "attack":
            enemy.health = enemy.health - player.attack()
            if player.health < 0:
                print("You have died.")
                quit()

        elif input() == "heal":
            player.health = player.health + player.heal()
            print(f"You now have {player.health} health remaining.\n")

        else:
            print("Invalid response. What would you like to do?\nAttack\nRun")

        player.health = player.health - enemy.attack()
        print(f"You have {player.health} health remaining.\n")

    print(f"You have defeated {enemy.name}!")

def play():
    print("------------ Welcome to Simple RPG ------------\n")

    time.sleep(1)

    print("Please enter your character name: \n")

    player = Player(input(), 1, 100, 0)

    while(True):
        encounter(player)

    print(player.name)

    player.attack()

if __name__ == '__main__':
    play()
