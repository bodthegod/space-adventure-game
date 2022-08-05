# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def start_game_select():
    """
    Gives user options to start or end game
    """
    start_game_choice = input("Would you like to launch captain? yes/no \n")
    if start_game_choice == "yes":
        start_game()
    elif start_game_choice == "no":
        exit_game()
    else:
        print("To start or exit the game, enter the text 'yes' or 'no'.")


def choose_char_name():
    """
    User selects space name
    """
    char_name = input("Choose your alien name:\n")
    print(f"Greetings, {char_name}")


def weapon_select():
    """
    Gives user a class for their character
    """
    class_choice = random.choice([
        "Scavenger Laser",
        "Strange Glowing Pistol",
        "Rusty Railgun",
        "Uranium Repeater"])
    print("Your weapon shifts and clicks into gear, whirring ready to fire.")
    print(f"The {class_choice} speaks to you, levitating towards your fingertips")

#def start_game():

#def exit_game():

def main():
    """
    Main function to call all functions
    """
    choose_char_name()
    start_game_select()
    weapon_select()
    # start_game()
    # exit_game()

main()
