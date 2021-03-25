
import curses
import random
import time



skin = '6'
elien = "✡"
missile = '|'
score = 0
height = 30
width = 120

# ustawienia okienka
curses.initscr()
win = curses.newwin(height, width) # wys i szer
win.keypad(True)
curses.noecho() # nie reaguje na inne klawisze
curses.curs_set(False)
win.border(0)
win.nodelay(True) # nie czeka na kolejna akcje




hero = [(28, 45)] # startowe współrzędne


def create_eliens():
    alien_row = []
    for y in range(2,16,3):
        for x in range(3, 71, 9):
                alien_row.append((y, x))
    return alien_row

def draw_eliens(alien_row):
    for alien in alien_row:
        win.addch(alien[0], alien[1], elien)

def move_eliens(alien_row):
    for alien in alien_row:
        win.addch(alien[0], alien[1], ' ')
        alien.insert(alien[0], alien[1] + 1)
        win.addch(alien[0], alien[1] + 1, elien)
#
# def move(alien_row, y, x):
#     for alien in alien_row:
#         alien.insert(0, (y, x))

eliens = create_eliens()
draw_eliens(eliens)


while True:
    win.addstr(0, 4, 'Eliens.exe')
    win.addstr(0, 50, 'Score ' + str(score) + ' ')
    win.timeout(60)

    win.addch(hero[0][0], hero[0][1], skin)

    for i in range(len(eliens)):

        y = eliens[i][0]
        x = eliens[i][1]
        x += 1


        eliens.insert(i, (y, x))

        draw_eliens(eliens)

    if win.getch() == 27:
        break