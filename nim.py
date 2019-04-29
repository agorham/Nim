"""NIM Game.
Author: Andrew Gorham
Class: CSI-260-01
Assignment: Final Project

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import sys


class Game:
    """
    Class where any gameplay calculation and representation happens
    """
    def __init__(self):
        """
        Initializes game class
        """
        self._balls = 24
        self.total_balls = 24

    def __str__(self):
        """
        String representation of the game's current state
        :return: Strings describing game
        """
        print(f'There are {self.balls} balls in the Pool Pile')
        print(f'There are {self.total_balls - self.balls} balls in the Drop Pile')

    @property
    def balls(self):
        """
        Getter for balls property
        :return: balls
        """
        return self._balls

    @balls.setter
    def balls(self, amt):
        """
        Action of dropping balls using setter
        :param amt: the amount of balls being dropped
        """
        self._balls = self._balls - amt

    def game_state_ascii(self):
        """
        The ASCII representation of the game's current state
        :return: ASCII of Game
        """
        pool_pile = ''.join(['O' * i for i in range(self.balls)][-1:])
        drop_pile = ''.join(['O' * i for i in range(self.total_balls - self.balls)][-1:])
        print(f'Pool Pile: {pool_pile}')
        print(f'Drop Pile: {drop_pile}')
        print('`````````````````````````')

    def human_turn(self):
        """
        The behavior of the human on their turn in the game
        :return: drop correct number of balls and print the action
        """
        self.game_state_ascii()
        choice = input('How many balls do you want to drop? (1, 2, or 3)')
        if choice == '1':
            self.balls = 1
            if self.balls == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()
        elif choice == '2':
            self.balls = 2
            if self.balls == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()
        elif choice == '3':
            self.balls = 3
            if self.balls == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()

    def cpu_turn(self):
        """
        The behavior of the cpu on its turn in the game
        :return: drop correct number of balls and print the action
        """
        if self.balls % 4 == 3:
            self.balls = 3
            print('The CPU has dropped 3 balls')
            if self.balls == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()
        elif self.balls % 4 == 2:
            self.balls = 2
            print('The CPU has dropped 2 balls')
            if self.balls == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()
        elif self.balls % 4 == 1:
            self.balls = 1
            print('The CPU has dropped 1 ball')
            if self.balls == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()

    @staticmethod
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
