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