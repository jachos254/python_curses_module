import curses

class Game:
    def __init__(self, width, height):
        curses.initscr()
        self.width = width
        self.height = height
        screen = curses.newwin(width, height)
        screen.keypad(True)
        curses.noecho()
        curses.curs_set(False)
        screen.border(0)
        screen.nodelay(True)
        screen.timeout(-1)

Game(20, 60)

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Generator:
    def __init__(self):
        pass

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y