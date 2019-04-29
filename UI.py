"""User Interface for Nim"""
import sys
import nim

menu = """
1. Start Game
2. Print Rules
3. Exit
Choose:
"""

game_instance = nim.Game()  # Creates a new game instance for play


def print_rules():
    """
    Prints out the game rules in paragraph form.
    :return: rules string
    """

    rules = """
    There are a set amount of balls on the board (12).
    You and the computer take turns dropping the balls from
    the upper ball area, called the pool, to the lower ball area, called the dump.
    You can drop 1, 2 or 3 balls at a time. The one who drops the final ball is the winner
    """
    print(rules)


menu_dict = {'1': game_instance.human_turn,
             '2': print_rules,
             '3': sys.exit}


while True:
    user_choice = input(menu)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')
