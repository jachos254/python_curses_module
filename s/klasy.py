import curses

class Alien:

    score = 0
    def __init__(self, y, x, window):
        self.y = y
        self.x = x

        self.window = window


    def draw(self):
        skin = '#'
        self.window.addstr(self.y, self.x, skin)
        self.y += 1

    def check_colision(self, window):

        for rocket in window.rockets:
            if (rocket.x < self.x and
                rocket.x > self.x and
                rocket.y < self.y and
                rocket.y > self.y):

                window.rockets.remove(rocket)
                window.aliens.remove(self)
                Alien.score += 1

class Hero:
    def __init__(self, y, x, window):
        self.y = y
        self.x = x
        self.window = window

    def draw(self):
        skin = '8'
        self.window.addstr(self.y, self.x, skin)

class Generator:
    def __init__(self, window):
        for y in range(2, 16, 3):
            for x in range(3, 71, 9):
                window.aliens.append(Alien(y, x, window))

class Rocket:
    def __init__(self, y, x, window):
        self.y = y
        self.x = x
        self.window = window

    def draw(self):
        skin = '|'
        self.window.addstr(self.y, self.x, skin)

        self.y -= 2




