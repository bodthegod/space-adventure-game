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


class UserNumbers:
    """
    Number selection class for storyline advancements
    """
    def __init__(self, number_one, number_two, number_three, number_else):
        """
        Instancing 1, 2 and 3 number selection
        """
        self.number_one = number_one
        self.number_two = number_two
        self.number_three = number_three
        self.number_else = number_else
