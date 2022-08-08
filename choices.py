"""
Class to respond to user choices
"""
class UserChoices:
    """
    User choices class
    """
    def __init__(self, choice_yes, choice_no, choice_else):
        """
        Instancing yes or no choices
        """
        self.choice_yes = choice_yes
        self.choice_no = choice_no
        self.choice_else = choice_else


    def yes_choice(self):
        """
        Function runs if user selects yes
        """
        return f"\n{self.choice_yes} \n"


    def no_choice(self):
        """
        Function runs if user selects no
        """
        return f"\n{self.choice_no} \n"


    def else_choice(self):
        """
        Function runs if user selects choice other than yes or no
        """
        return f"\n{self.choice_else} \n"

class UserNumbers:
    """
    Number selection class for storyline advancements
    """
    def __init__(self, number_one, number_two, number_three):
        """
        Instancing 1, 2 and 3 number selection 
        """
        self.number_one = number_one
        self.number_two = number_two
        self.number_three = number_three


    def number_one(self):
        """
        Function runs if user selects 1
        """
        return f"\n{self.number_one} \n"


    def number_two(self):
        """
        Function runs if user selects 2
        """
        return f"\n{self.number_two} \n"


    def number_three(self):
        """
        Function runs if user selects 3
        """
        return f"\n{self.number_three} \n"

class UserNumbersElse:
    """
    Class for else statement in UserNumbers selection
    """
    def __init__(self):
        """
        Instancing else option if user selects other than 1, 2 or 3
        """
        self.number_else = "Enter 1, 2 or 3 to choose a route."

    def user_number_else(self):
        """
        Function runs when user selects other than 1, 2 or 3
        """
        return f"\n{self.number_else}"
