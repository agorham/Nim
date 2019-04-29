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
    def __init__(self):
        self.balls = 24
        self.total_balls = 24

    def __str__(self):
        print(f'There are {self.ball_count()} balls in the Pool Pile')
        print(f'There are {self.total_balls - self.ball_count()} balls in the Drop Pile')

    def ball_count(self):
        return self.balls

    def game_state_ascii(self):
        pool_pile = ''
        drop_pile = ''
        for i in range(self.ball_count()):
            pool_pile = pool_pile + 'O'
        for i in range(self.total_balls - self.ball_count()):
            drop_pile = drop_pile + 'O'
        print(f'Pool Pile: {pool_pile}')
        print(f'Drop Pile: {drop_pile}')
        print('`````````````````````````')

    def ball_drop(self, amt):
        self.balls = self.balls - int(amt)

    def human_turn(self):
        self.game_state_ascii()
        choice = input('How many balls do you want to drop? (1, 2, or 3)')
        if choice == '1':
            self.ball_drop(1)
            if self.ball_count() == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()
        elif choice == '2':
            self.ball_drop(2)
            if self.ball_count() == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()
        elif choice == '3':
            self.ball_drop(3)
            if self.ball_count() == 0:
                print('Congrats, you win!')
                sys.exit()
            self.cpu_turn()

    def cpu_turn(self):
        """
        The behavior of the cpu on its turn in the standard game
        :return: drop correct number of balls and print the action
        """
        if self.ball_count() % 4 == 3:
            self.ball_drop(3)
            print('The CPU has dropped 3 balls')
            if self.ball_count() == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()
        elif self.ball_count() % 4 == 2:
            self.ball_drop(2)
            print('The CPU has dropped 2 balls')
            if self.ball_count() == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()
        elif self.ball_count() % 4 == 1:
            self.ball_drop(1)
            print('The CPU has dropped 1 ball')
            if self.ball_count() == 0:
                print('The computer has won')
                sys.exit()
            else:
                self.human_turn()

