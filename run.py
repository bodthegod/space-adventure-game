# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import time
import random
from choices import UserChoices

# slowprint taken from https://www.codegrepper.com/code-examples/python/python+slow+print
def slowprint(strings):
	for text_c in strings + '\n \n':
		sys.stdout.write(text_c)
		sys.stdout.flush()
		time.sleep(0./20)


def spacing():
    """
    Creates spacing between dialogue to improve readability of game
    """
    print()

spacing()

def game_prologue():
    """
    Displays game prologue text and lore to user
    """
    spacing()

    slowprint(
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
    spacing()

    start_game_choices = UserChoices(
        "*spooling* Whirring up engines *humming* \n",
        "Shutting down systems \n",
        "To start or exit the game, enter the text 'yes' or 'no'. \n"
        )
    
    start_game_input = input("Would you like to launch captain? yes/no \n")
    
    spacing()

    if start_game_input == "yes":
        slowprint(start_game_choices.choice_yes)
    elif start_game_input == "no":
        slowprint(start_game_choices.choice_no)
        exit_game()
    else:
        slowprint(start_game_choices.choice_else)
        start_game_select()


def game_instructions_select():
    """
    Allows player to select if they want instructions 
    """
    spacing()

    game_instructions_choices = UserChoices(
        "Since you're here, we are going to tell the tale of the galaxy... \n",
        "Who needed to read that anyways... \n",
        "Please select yes or no. \n") 
     
     
    game_instructions_input = input("Do you want to hear the story of the galaxy before you begin? (yes/no) \n")
    
    spacing()

    if game_instructions_input == "yes":
        slowprint(game_instructions_choices.choice_yes)
        game_instructions()
    elif game_instructions_input == "no":
        slowprint(game_instructions_choices.choice_no)
        second_functions()
    else:
        slowprint(game_instructions_choices.choice_else)
        game_instructions_select()


def game_instructions():
    """
    Gives guide to the player about the game
    """
    slowprint("\n" 
    "The year is 3076, and humanity is on it's last legs... \n"
    "You awake from a cryofrozen chamber inside your ancient ship... \n"
    "Your ship is outdated as you have been frozen for over 500 years... \n")

    slowprint("\n" 
    "You are the last Super Soldier... \n"
    "Explore the options and choose wiseley... \n"
    "It may be the last choice you make... \n")

    second_functions()


def choose_char_name():
    """
    User selects space name
    """
    char_name = input("Choose your name, survivor: \n")
    spacing()
    slowprint(f"*Your ship greets you* Greetings, {char_name}")


def char_class_info():
    """
    Prints class info and start to game lore
    """
    slowprint("\n"
    "*bzzt* Hey, you! *bzzt* \n"
    "*bzzt* In order to reclaim the galaxy, you may need one of these! *bzzt* \n"
    "*bzzt* Walk over there to your arsenal and allow it to choose you. *bzzt* \n")


def weapon_text():
    """
    Requests the player if they want the weapon to be selected
    """
    request_weapon = input("It's time to walk over to the arsenal, would you like to choose a weapon? (yes/no)\n")
    
    spacing()
    
    if request_weapon == "yes":
        slowprint("Your weapon shifts and clicks into gear, whirring ready to fire. \n")
    elif request_weapon == "no":
        slowprint("I can't help the galaxy without a weapon... \n")
        exit_game()
    else:
        slowprint("Please select yes or no \n")
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

    slowprint(f"The {random_class_choice} speaks to you, levitating towards your fingertips \n")


def first_ship_storyline():
    """
    Displays first ship storyline to user
    """
    slowprint("\n"
    "*bzzt* That's it, you remember how to start one of these, don't you? *bzzt* \n"
    "*bzzt* You don't? just hit that big red button... *clonk* woahhhh! *bzzt* \n"
    "*Female AI voice* 'Quantum travel initiated' *spooling* \n")

    slowprint("\n"
    "*The ship sparks and sputters, inputting the co-ordinates of the distress beacon* \n"
    "*Time stops, the ship warps and a second later you appear in a new solar system* \n"
    "*bzzt* Is that you? *bzzt* \n")


def distress_beacon_mission():
    """
    Gives the user options to solve the mission
    """
    slowprint("\n"
    "'Yeah, it's me.' \n"
    "*bzzt* Finally!, we're under attack and there are bidalgan pirates boarding our ship! *bzzt* \n"
    "'I'm docking now' / end of transmission \n")

    slowprint("\n"
    "You dock the ship, and there are 3 pirates aiming in your direction, what do you do? \n"
    "(1) Start an attack on the pirates \n"
    "(2) Set up an ambush \n"
    "(3) Wait and listen for conflict \n")

    select_answer = input("What do you do? (1,2,3) \n")
    
    spacing()

    if "1" in select_answer:
        slowprint("You fire your weapon, tagging and eliminating all three pirates in a flurry")
    elif "2" in select_answer:
        slowprint("\n"
        "You hold the corner, the squad approach you and fire at you \n"
        "Your weapon overloads with energy, firing at it's own will and eliminates the targets \n"
        "'Woah...' \n")
    elif "3" in select_answer:
        slowprint("\n"
        "You wait and listen, hearing alien noises and footsteps towards you \n"
        "Your weapon overloads with energy, firing at it's own will and eliminates the targets \n"
        "'What was that...' \n")
    else:
        slowprint("Enter 1, 2 or 3 to choose a route.")
        distress_beacon_mission()


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


def second_functions():

    choose_char_name()
    char_class_info()
    weapon_text()
    weapon_select()
    first_ship_storyline()
    distress_beacon_mission()
    

main()
exit_game_select()