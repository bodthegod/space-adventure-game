# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def choose_char_name():
    """
    User selects space name
    """
    char_name = input("Choose your alien name:\n")
    print(f"Greetings, {char_name}")


choose_char_name()