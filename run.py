# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import time
import random
from choices import UserChoices
from choices import UserNumbers


# slowprint taken from
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# and https://www.codegrepper.com/code-examples/python/python+slow+print
def slowprint(strings):
    for text_c in strings + '\n \n':
        sys.stdout.write(text_c)
        sys.stdout.flush()
        time.sleep(0/20)


def spacing():
    """
    Creates spacing between dialogue to improve readability of game
    """
    print()

spacing()
# ASCII art taken from https://www.asciiart.eu/space/spaceships
# and https://patorjk.com/software/taag/#p=testall&f=4Max&t=Space%20Adventure
print(r"""

     .  . '    .
      '   .            . '            .                +
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs

                  _
                 /_`_  _  _  _   /_/ _/  _  _ _/_   __
                ._//_//_|/_ /_' / //_/|//_'/ // /_///_'
                  /
""")


def game_prologue():
    """
    Displays game prologue text and lore to user
    """
    spacing()

    slowprint(
        "\n"
        "incoming transmission... \n"
        "*bzzt* Survivor? Are you there? *bzzt* \n"
        "*bzzt* We have been waiting for you to wake up *bzzt* \n"
        "The Galaxy is in dire need of your help. *bzzt* \n"
        "*bzzt* We know you have the skills to assist the Galaxy. *bzzt* \n"
        "*bzzt* We are sending you the distress beaconco-ordinates now"
        "*bzzt* \n"
        "end of transmission \n"
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

    game_instructions_input = input("Do you want to hear the story of the"
                                    "galaxy before you begin? (yes/no) \n")

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
              "You awake from a cryofrozen chamber inside your ancient"
              " ship... \n"
              "Your ship is outdated as you have been frozen for over"
              "500 years... \n")

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
              "*bzzt* In order to reclaim the galaxy, you may need"
              " one of these! *bzzt* \n"
              "*bzzt* Walk over there to your arsenal and allow it"
              " to choose you. *bzzt* \n")


def weapon_text():
    """
    Requests the player if they want the weapon to be selected
    """
    request_weapon = input("It's time to walk over to the arsenal, would you"
                           " like to choose a weapon? (yes/no)\n")

    spacing()

    if request_weapon == "yes":
        slowprint("Your weapon shifts and clicks into gear,"
                  " whirring ready to fire. \n")
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

    slowprint(f"The {random_class_choice} speaks to you,"
              " levitating towards your fingertips \n")


def first_ship_storyline():
    """
    Displays first ship storyline to user
    """
    slowprint("\n"
              "*bzzt* That's it, you remember how to start "
              " one of these, don't you? *bzzt* \n"
              "*bzzt* You don't? just hit that big red button..."
              " *clonk* woahhhh! *bzzt* \n"
              "*Female AI voice* 'Quantum travel initiated' *spooling* \n")

    slowprint("\n"
              "*The ship sparks and sputters, inputting the co-ordinates"
              " of the distress beacon* \n"
              "*Time stops, the ship warps and a second later you appear"
              " in a new solar system* \n"
              "*bzzt* Is that you? *bzzt* \n")

    slowprint("\n"
              "You: 'Yeah, it's me.' \n"
              "*bzzt* Finally!, we're under attack and there are bidalgan"
              " pirates boarding our ship! *bzzt* \n"
              "You: 'I'm docking now' / end of transmission \n")


def distress_beacon_mission():

    """
    Gives the user options to solve the mission
    """
    distress_mission_choices = UserNumbers(
        "You fire your weapon, tagging and eliminating all three pirates"
        " in a flurry",
        "You hold the corner, the squad approach you and fire at you \n"
        "Your weapon overloads with energy, firing at it's own will and"
        " eliminates the targets \n"
        "You: 'Woah...' \n",
        "You wait and listen, hearing alien noises and footsteps towards"
        " you \n"
        "Your weapon overloads with energy, firing at it's own will and"
        " eliminates the targets \n"
        "You: 'What was that...' \n",
        "Enter 1, 2 or 3 to choose a route."

    )

    slowprint("\n"
              "You dock the ship, and there are 3 pirates aiming in your"
              " direction, what do you do? \n"
              "(1) Start an attack on the pirates \n"
              "(2) Set up an ambush \n"
              "(3) Wait and listen for conflict \n")

    select_answer = input("Select (1,2,3) \n")

    spacing()

    if "1" in select_answer:
        slowprint(distress_mission_choices.number_one)
        distress_beacon_storyline()
    elif "2" in select_answer:
        slowprint(distress_mission_choices.number_two)
        distress_beacon_storyline()
    elif "3" in select_answer:
        slowprint(distress_mission_choices.number_three)
        distress_beacon_storyline()
    else:
        slowprint(distress_mission_choices.number_else)
        distress_beacon_mission()


def distress_beacon_storyline():
    """
    Displays distress beacon storyline to player
    """
    slowprint("\n"
              "There is an eerie silence... what were they? \n"
              "*cockpit door clonks and beeps, the alien over the ship"
              " intercom emerges* \n")

    slowprint("\n"
              "'Thank you, soldier. Our ship was taken over a few hours"
              " ago and it's been dead in the water.'\n"
              "'Bidalgan pirates are one of the most dangerous species"
              " in the Galaxy, I saw your signature appear on my radar' \n"
              "'How did you?...'\n")

    slowprint("\n"
              "You: 'I don't understand it either, but it's best we don't"
              " question it.' \n"
              "'We still need assistance, the Bidalgans reside on planet"
              " Bid and they're quickly conquering all power in the galaxy' \n"
              "'Will you help us?' \n")


def distress_beacon_select():
    """
    Allows player to select the storyline they want to go with
    """
    spacing()

    distress_beacon_choices = UserChoices(
        "You nod your head, agreeing to help \n",
        "You shake your head, choosing your own path \n",
        "Please select yes or no. \n")

    distress_beacon_input = input("Do you want to help the Galaxy?"
                                  " (yes/no) \n")

    spacing()

    if distress_beacon_input == "yes":
        slowprint(distress_beacon_choices.choice_yes)
        planet_invasion_storyline()
    elif distress_beacon_input == "no":
        slowprint(distress_beacon_choices.choice_no)
        bounty_hunt_storyline()
    else:
        slowprint(distress_beacon_choices.choice_else)
        distress_beacon_select()


def planet_invasion_storyline():
    """
    Displays planet invasion storyline to the user
    """
    slowprint("\n"
              "You know you are ready to take the next step in"
              " assisting the galaxy \n"
              "*The friendly alien sees you nod your head* \n")

    slowprint("\n"
              "*The ship sparks back to life* 'Your ship looks outdated,"
              " and I don't think we have the weapons on board"
              " to take another attack' \n"
              "'This ship is one of the top of the line fighting"
              " vessels,"
              " we would of had them if it wasn't for the EMP they hit us"
              " with...' \n"
              "'I suggest you take our ship, Soldier. You look capable to"
              " take the Bidalgans alone, so here.' \n"
              "*He hands you a glowing ship key* \n")

    slowprint("\n"
              "*The key resonates in your hand, it feels familiar* \n"
              "'We will take your old ship, this is for the greater"
              " good of the galaxy. Thank you soldier.' \n"
              "'The co-ordinates of Planet Bid are on the intercom,"
              " the ship will warp you once we dock your old ship.' \n"
              "You nod again, knowing what must be done, the alien"
              " walks away \n"
              "*The alien shouts* 'Good luck, you are our only hope.' \n")


def ship_storyline_select():
    """
    Gives the user options to solve the mission
    """
    spacing()

    ship_storyline_choices = UserNumbers(
        "You press the big red button and there is a weird glow around"
        " the outer of the ship \n"
        "Time bends, a black hole emerges and you appear in a new system,"
        " greeted with three purple stars \n"
        "There is conflict everywhere, space stations covered in green"
        " hellfire",
        "You pull the white lever and the ship sparks, time and space"
        " folds and you enter a new system \n"
        "There are three purple stars, and the whole system is in"
        " conflict \n"
        "You see many space stations, covered in green hellfire",
        "Your new ship starts recalculating the route, I don't think"
        " that was a good choice... \n"
        "*You are warped to a completely new system, the ship display"
        " reads *9288 LY from initial warp* \n"
        "*You receive a bounty hunting mission in your system* \n",
        "Enter 1, 2 or 3 to choose a storyline."

    )

    slowprint("\n"
              "Your new ship looks unfamiliar, as if it is from a"
              " completely different"
              "time era than you \n"
              "What do you do? \n")
    slowprint("\n"
              "(1) Press the big red button you previously pressed \n"
              "(2) Pull the white lever \n"
              "(3) Press the button labelled '⎅⍜ ⋏⍜⏁ ⌿⍀⟒⌇⌇' \n")
# Alien text comes from https://lingojam.com/AlienLanguage
    select_answer = input("Select (1,2,3) \n")

    if "1" in select_answer:
        slowprint(ship_storyline_choices.number_one)
        planet_invasion_storyline_two()
    elif "2" in select_answer:
        slowprint(ship_storyline_choices.number_two)
        planet_invasion_storyline_two()
    elif "3" in select_answer:
        slowprint(ship_storyline_choices.number_three)
        bounty_hunt_storyline()
    else:
        slowprint(ship_storyline_choices.number_else)
        ship_storyline_select()

    spacing()
# Add flaming sword to planet bid tower of rin and add code
#  (2681 combination) question


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
    distress_beacon_select()
    ship_storyline_select()


main()
exit_game_select()
