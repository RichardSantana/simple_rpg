## A simple RPG game by Richard Santana ##

## The game's characters ##

from characters import Player, Enemy
import time

def encounter(player):

    time.sleep(1)

    if player.exp > 160:
        enemy = Enemy("Elf", 1.35, 40, 50)

    elif player.exp > 280:
        enemy = Enemy("Orc", 1.65, 100, 80)

    elif player.exp > 400:
        enemy = Enemy("Dragon", 2, 200, 1000)

    else:
        enemy = Enemy("Imp", 1, 20, 20)

    print(f"You've encountered an {enemy.name}!\n")

    time.sleep(1)

    while enemy.health > 0:
        time.sleep(1)

        player_move = input("What would you like to do?\nAttack\nHeal\nRun\n\n")

        if (player_move != "attack") and (player_move != "heal") and (player_move != "run"):
            print("Invalid response.\n")
            continue

        else:
            if player_move == "attack":
                enemy.health = enemy.health - player.attack()

            if player_move == "heal":
                player.health = player.health + player.heal()
                print(f"You now have {player.health} health remaining.\n")

            if player_move == "run":
                print("You have run away!\n")
                return

        player.health = player.health - enemy.attack()
        print(f"You have {player.health} health remaining.\n")

        if player.health <= 0:
            print("You have died.")
            quit()

    print(f"You have defeated {enemy.name}!\nYou have gained {enemy.exp} experience!")

    if enemy.name == "Dragon":
        print("You have won!")
        quit()

    player.exp = player.exp + enemy.exp

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
