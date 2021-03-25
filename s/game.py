import curses
from klasy import Alien, Hero, Generator, Rocket

class Game:
    rockets = []
    aliens = []
    lost = False
    score = 0
    def __init__(self, height, width):


        curses.initscr()
        self.window = curses.newwin(height, width)
        self.window.border(0)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.window.keypad(1)


        hero = Hero(self, 28, 60)
        generator = Generator(self)
        rocket = None

        while True:
            self.window.clear()
            self.window.border(0)



            event = self.window.getch()


            if event == 27:
                break

            if event == curses.KEY_LEFT:
                hero.x -= 1
            elif event == curses.KEY_RIGHT:
                hero.x += 1
            elif event == curses.KEY_UP:
                self.rockets.append(Rocket(self, hero.x + 1, hero.y))


            self.window.timeout(60)

            for alien in self.aliens:

                alien.draw()
                alien.check_collision(self)

                # if (alien.y > hero.y):
                #     break


            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: hero.draw()