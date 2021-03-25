
#IMPORTY
import curses
import random
import time



snake_piece = '卐'
fruit_piece = "✡"
rocket_avatar = '|'

# ustawienia okienka
curses.initscr()
win = curses.newwin(20, 60) # wys i szer
win.keypad(True)
curses.noecho() # nie reaguje na inne klawisze
curses.curs_set(False)
win.border(0)
win.nodelay(True) # nie czeka na kolejna akcje


# sznek i żarcie, uzywamy krotki

snake = [(18, 30), (18, 29), (18, 28)] # startowe współrzędne szneka
# food = (15, 5) # pierwsze jedzonko


# win.addch(food[0], food[1], fruit_piece)          # to samo dla jedzonka food0 i food1 pierwsza i druga wsplorzedna z krotki
# logika szneka
margin = 3
width = 3
for y in range(margin, 10, width):
    for x in range(margin, 60 - width, width):
        food = (y, x)
        win.addch(food[0], food[1], fruit_piece)

win.addch(snake[0][0], snake[0][1], snake_piece)
win.addch(snake[1][0], snake[1][1], snake_piece)
win.addch(snake[2][0], snake[2][1], snake_piece)


score = 0
EXIT = 27      #27 to nr escape w module curses
# key = curses.KEY_RIGHT

def rocket(x):

    y = 17
    rocket = [(y, x)]

    while True:

        win.addch(rocket[0][0], rocket[0][1], rocket_avatar)
        y -= 1

        rocket.insert(0, (y, x))

        if rocket[0][0] == food[0] - 1:

            remove = rocket.pop()
            win.addch(remove[0], remove[1], ' ')
            break
        remove = rocket.pop()
        win.addch(remove[0], remove[1], ' ')
        if y == 0:
            break




# while key != EXIT:
while True:
    win.addstr(0, 4, 'Szpejs_Invaders.exe')
    win.addstr(0, 50, 'Score ' + str(score) + ' ')
    # win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # dodanie prędkości
    # win.timeout(150 - (len(rockets)) // 5 + len(rockets) // 10 % 120)
    win.timeout(-1)
    # win.timeout(60)


    key = win.getch()
    # key = event if event != -1 else prev_key
    # #
    # if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, EXIT]:  #program zostaje na wczesniejszym klawiszu
    #     key = prev_key
    if key == 27:
        break

    win.addch(snake[0][0], snake[0][1], snake_piece)

    #kolejne koordynaty, poczatkowe z pierwszej krotki
    y = snake[0][0]
    x = snake[0][1]


    # y i x dół i w prawo

    if key == curses.KEY_UP:
        rocket(x)
        score += 1


    if key == curses.KEY_RIGHT:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        x += 1 if x < 58 else 0
        snake.insert(0, (18, x))
        win.addch(snake[0][0], snake[0][1], snake_piece)

    if key == curses.KEY_LEFT:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        x -= 1 if x > 2 else 0
        snake.insert(0, (18, x))
        win.addch(snake[0][0], snake[0][1], snake_piece)

    # rocket.insert(0, (y, rocket[0][1]))
    # snake.insert(0, (snake[0][0], x))



    # snake.insert(0, (y, x))

    # uderzenie w granice
    #
    # if y == 0: break
    # if y ==19: break
    # if x == 0: break
    # if x == 59: break


    # if rocket[0][0] == food:
    #
    #     last_rocket = rocket.pop()
    #     win.addch(last_rocket[0], last_rocket[1], ' ')
    #     last = snake.pop()
    #     win.addch(last[0], last[1], ' ')
    #
    # else:
    #     # ruch szneka
    #     last_rocket = rocket.pop()
    #     win.addch(last_rocket[0], last_rocket[1], ' ')
    #     last = snake.pop()
    #     win.addch(last[0], last[1], ' ')





           # to samo dla jedzonka food0 i food1 pierwsza i druga wsplorzedna z krotki


curses.endwin() # konczy okno

# print(f'Final score = {score}')