"""User Interface for Nim"""
import sys
import nim

menu = """
1. Start Game
2. Print Rules
3. Exit
Choose:
"""
game_instance = nim.Game()


def human_turn():  # TODO
    game_instance.game_state_ascii()
    choice = input('How many balls do you want to drop? (1, 2, or 3)')

    if choice == 1:
        game_instance.ball_drop(1)
        if game_instance.ball_count() == 0:
            print('Congrats, you win!')
            end_game()
        game_instance.cpu_turn()
    elif choice == 2:
        game_instance.ball_drop(2)
        if game_instance.ball_count() == 0:
            print('Congrats, you win!')
            end_game()
        game_instance.cpu_turn()
    elif choice == 3:
        game_instance.ball_drop(3)
        if game_instance.ball_count() == 0:
            print('Congrats, you win!')
            end_game()
        game_instance.cpu_turn()
    else:
        raise ValueError('Not a Valid Choice')


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


def end_game():
    """
    Exits the program.
    :return: Exit command
    """
    sys.exit()


menu_dict = {'1': human_turn,
             '2': print_rules,
             '3': end_game}

while True:
    user_choice = input(menu)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')
