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


menu_dict = {'1': game_instance.human_turn,
             '2': game_instance.print_rules,
             '3': sys.exit}


while True:
    user_choice = input(menu)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')
