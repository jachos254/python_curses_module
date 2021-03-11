#IMPORTY
import curses
import random

# ustawienia okienka
curses.initscr()
win = curses.newwin(20, 60) # wys i szer
win.keypad(True)
curses.noecho() # nie reaguje na inne klawisze
curses.curs_set(False)
win.border(0)
win.nodelay(True) # nie czeka na kolejna akcje


# sznek i żarcie, uzywamy krotki

snake = [(5, 10), (5, 9), (5, 8)] # startowe współrzędne szneka
food = (10, 20) # pierwsze jedzonko

win.addch(food[0], food[1], '?')          # to samo dla jedzonka food0 i food1 pierwsza i druga wsplorzedna z krotki
# logika szneka
score = 3

EXIT = 27      #27 to nr escape w module curses
key = curses.KEY_RIGHT

while key != EXIT:
    win.addstr(0, 4, 'Sznek.exe')
    win.addstr(0, 50, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # dodanie prędkości

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, EXIT]:  #program zostaje na wczesniejszym klawiszu
        key = prev_key

    #kolejne koordynaty, poczatkowe z pierwszej krotki
    y = snake[0][0]
    x = snake[0][1]
    # y i x dół i w prawo
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1

    snake.insert(0, (y, x))  #nowa głowa, przesuwa cała tuple

    # uderzenie w granice

    if y == 0: break
    if y ==19: break
    if x == 0: break
    if x == 59: break

    # na siebie
    if snake[0] in snake[1:]: break
    #na jedzonko
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (random.randint(1, 18), random.randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], 'o')
    else:
        # ruch szneka
        last = snake.pop()
        win.addch(last[0], last[1], ' ')



    win.addch(snake[0][0], snake[0][1], '#')          # to samo dla jedzonka food0 i food1 pierwsza i druga wsplorzedna z krotki






curses.endwin() # konczy okno


print(f'Final score = {score}')