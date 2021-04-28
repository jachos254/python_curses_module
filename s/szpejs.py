
import  curses
import random

hero_avatar = '#'
elien_avatar = '*'
rocket_avatar = '|'

curses.initscr()
win = curses.newwin(20, 60)
win.keypad(True)
curses.noecho()
curses.curs_set(False)
win.border(0)
win.nodelay(True)

hero = [(18, 30)]

score = 0

EXIT = 27
key = curses.KEY_RIGHT

while key != EXIT:
    win.addstr(0, 4, 'Szpejs_Inwejders.exe')
    win.addstr(0, 50, 'Score ' + str(score) + ' ')


    prev_key = key

    event = win.getch()
    key = event if event != -1 else prev_key


    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, EXIT]:  #program zostaje na wczesniejszym klawiszu
        key = prev_key

    x = hero[0][1]
    # if key == curses.KEY_RIGHT:
    #     x += 1 if x < 55 else 0
    # if key == curses.KEY_LEFT:
    #     x -= 1 if x > 5 else 0

    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1

    hero.insert(0, (1, x))
    last = hero.pop()
    win.addch(last[0], last[1], ' ')


    win.addch(hero[0][0], hero[0][1], hero_avatar)


curses.endwin()


