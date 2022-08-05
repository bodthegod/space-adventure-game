# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import random


def game_prologue():
    """
    Displays game prologue text and lore to user
    """
    print("incoming transmission... *bzzt* Survivor? Are you there? *bzzt*")
    print("*bzzt* We have been waiting for you to wake up, and the Galaxy is in dire need of your help. *bzzt*")
    print("*bzzt* We know you have the skills to assist the Galaxy. *bzzt*")
    print("*bzzt* We are sending you the distress beacon co-ordinates now *bzzt* \ end of transmission")

def start_game_select():
    """
    Gives user options to start or end game
    """
    start_game_choice = input("Would you like to launch captain? yes/no \n")
    if start_game_choice == "yes":
        print("*spooling* Whirring up engines *humming*")
        # start_game()
    elif start_game_choice == "no":
        print("Shutting down systems")
        exit_game()
    else:
        print("To start or exit the game, enter the text 'yes' or 'no'.")
        start_game_select()


def choose_char_name():
    """
    User selects space name
    """
    char_name = input("Choose your alien name:\n")
    print(f"Greetings, {char_name}")

def char_class_info():
    """
    Prints class info and start to game lore
    """
    print('"Hey, you!"')
    print('"In order to take over the galaxy, you may need one of these!"')
    print('"Walk over there to your arsenal and allow it to choose you."')
    
def weapon_select():
    """
    Gives user a class for their character (random)
    """
    class_choice = [
        "Scavenger Laser",
        "Strange Glowing Pistol",
        "Rusty Railgun",
        "Uranium Repeater"]

    random_class_choice = random.choice(class_choice)

    print("Your weapon shifts and clicks into gear, whirring ready to fire.")
    print(f"The {class_choice} speaks to you, levitating towards your fingertips")

# def start_game():
#     """
#     Starts game
#     """
#     main()


def exit_game():
    """
    Exits game
    """
    sys.exit()

def main():
    """
    Main function to call all functions
    """
    
    game_prologue()
    start_game_select()
    choose_char_name()
    char_class_info()
    weapon_select()
    

main()
