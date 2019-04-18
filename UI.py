import curses


class GameInterface:
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

