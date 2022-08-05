# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import random
from items import items


def game_prologue():
    """
    Displays game prologue text and lore to user
    """
    print(
        "\n"
        "incoming transmission... *bzzt* Survivor? Are you there? *bzzt* \n"
        "*bzzt* We have been waiting for you to wake up, and the Galaxy is in dire need of your help. *bzzt* \n"
        "*bzzt* We know you have the skills to assist the Galaxy. *bzzt* \n"
        "*bzzt* We are sending you the distress beacon co-ordinates now *bzzt* \ end of transmission \n"
    )


def start_game_select():
    """
    Gives user options to start or end game
    """
    start_game_choice = input("Would you like to launch captain? yes/no \n")
    if start_game_choice == "yes":
        print("*spooling* Whirring up engines *humming* \n")
    elif start_game_choice == "no":
        print("Shutting down systems \n")
        exit_game()
    else:
        print("To start or exit the game, enter the text 'yes' or 'no'. \n")
        start_game_select()


def game_instructions_select():
    """
    Allows player to select if they want instructions 
    """
    game_instructions_choice = input("Do you want to hear the story of the galaxy before you begin? (yes/no) \n")
    if game_instructions_choice == "yes":
        game_instructions()
    elif game_instructions_choice == "no":
        print("Who needed to read that anyways... \n")
        choose_char_name()
    else:
        print("Please select yes or no. \n")
        game_instructions_choice()


def game_instructions():
    """
    Gives guide to the player about the game
    """
    print("\n Since you're here, we are going to tell the tale of the galaxy... \n")
    print("The year is 3076, and humanity is on it's last legs...")
    print("You awake from a cryofrozen chamber inside your ancient ship...")
    print("Your ship is outdated as you have been frozen for over 500 years... \n")

    print("You are the last Super Soldier...") 
    print("Explore the options and choose wiseley...")
    print("It may be the last choice you make... \n")


def choose_char_name():
    """
    User selects space name
    """
    char_name = input("Choose your name, survivor: \n")
    print(f"Greetings, {char_name}")


def char_class_info():
    """
    Prints class info and start to game lore
    """
    print('*bzzt* Hey, you! *bzzt*')
    print('*bzzt* In order to reclaim the galaxy, you may need one of these! *bzzt*')
    print('*bzzt* Walk over there to your arsenal and allow it to choose you. *bzzt*')


def weapon_text():
    """
    Requests the player if they want the weapon to be selected
    """
    request_weapon = input("It's time to walk over to the arsenal, would you like to choose a weapon? (yes/no)\n")
    if request_weapon == "yes":
        print("Your weapon shifts and clicks into gear, whirring ready to fire. \n")
    elif request_weapon == "no":
        print("I can't help the galaxy without a weapon... \n")
        exit_game()
    else:
        print("Please select yes or no \n")
        weapon_text()


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

    print(f"The {random_class_choice} speaks to you, levitating towards your fingertips \n")


def first_ship_storyline():
    """
    Displays first ship storyline to user
    """
    print("*bzzt* That's it, you remember how to start one of these, don't you? *bzzt*")
    print("*bzzt* You don't? just hit that big red button... *clonk* woahhhh! *bzzt* \n")
    print("*Female AI voice* 'Quantum travel initiated' *spooling* \n")

    print("*The ship sparks and sputters, inputting the co-ordinates of the distress beacon*")
    print("*Time stops, the ship warps and a second later you appear in a new solar system* \n")
    print("*bzzt* Is that you? *bzzt* \n")


def distress_beacon_mission():
    """
    Gives the user options to solve the mission
    """
    print("'Yeah, it's me.' \n")
    print("*bzzt* Finally!, we're under attack and there are bidalgan pirates boarding our ship! *bzzt*")
    print("\n 'I'm docking now' / end of transmission \n")

    print("You dock the ship, and there are 3 pirates aiming in your direction, which way do you go?")
    print("(1) Start an attack on the pirates \n")
    print("(2) Set up an ambush \n")
    print("(3) Wait and listen for conflict \n")

    select_answer = input("What do you do? (1,2,3) \n")

    if "1" in select_answer:
        print("You fire your weapon, tagging and eliminating all three pirates in a flurry")
    elif "2" in select_answer:
        print("You hold the corner, the squad approach you and fire at you")
        print("Your weapon overloads with energy, firing at it's own will and eliminates the targets")
        print("'Woah...'")
    elif "3" in select_answer:
        print("You wait and listen, hearing alien noises and footsteps towards you")
        print("Your weapon overloads with energy, firing at it's own will and eliminates the targets")
        print("'What was that...'")
    else:
        print("Enter 1, 2 or 3 to choose a route.")
        distress_beacon_mission()

def open_items():
    """
    Player can view items by pressing I
    """
    user_button = input(" ")
    if "i" in user_button:
        show_items()

def show_items():
    """
    Shows items to user in console
    """
    print(items)

def exit_game_select():
    """
    Player can exit game by pressing X
    """
    user_button = input(" ")
    if "x" in user_button:
        exit_game()


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
    game_instructions_select()
    open_items()
    char_class_info()
    weapon_text()
    weapon_select()
    first_ship_storyline()
    distress_beacon_mission()
    

main()
