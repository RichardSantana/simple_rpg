## A simple RPG game by Richard Santana ##

## The game's characters ##

from characters import Player, Enemy
import time

def encounter(player):

    time.sleep(1)

    enemy = Enemy("Imp", 1, 20, 20)

    print("You've encountered an enemy!\n")

    time.sleep(1)

    while enemy.health > 0:
        time.sleep(1)

        player_move = input("What would you like to do?\nAttack\nHeal\nRun\n")

        if (player_move != "attack") and (player_move != "heal") and (player_move != "run"):
            print("Invalid response.\n")
            print(player_move)
            continue

        else:
            if player_move == "attack":
                enemy.health = enemy.health - player.attack()
                if player.health < 0:
                    print("You have died.")
                    quit()

            if player_move == "heal":
                player.health = player.health + player.heal()
                print(f"You now have {player.health} health remaining.\n")

            if player_move == "run":
                print("You have run away!\n")
                return

        player.health = player.health - enemy.attack()
        print(f"You have {player.health} health remaining.\n")

    print(f"You have defeated {enemy.name}!\nYou have gained {enemy.exp} experience!")

def play():
    print("------------ Welcome to Simple RPG ------------\n")

    time.sleep(1)

    print("Please enter your character name: \n")

    player = Player(input(), 1, 100, 100)

    while(True):
        encounter(player)

    print(player.name)

    player.attack()

if __name__ == '__main__':
    play()
