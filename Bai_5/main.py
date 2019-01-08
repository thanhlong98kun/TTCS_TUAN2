import curses
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
import time
import random

def game():
    win = curses.initscr()
    win.keypad(1)           # Cho phep su dung cac phim dat biet nhu: up down left right
    curses.curs_set(0)      # Tat con tro nhap nhay
    win.nodelay(1)          # Vong lap van chay khi gap ham nhap 1 ki tu nhu win.getch()

    max_y, max_x = win.getmaxyx()
    head = [1, 1]
    body = [head[:]] * 5
    deadcell = body[-1][:]
    direction = 0   # 0: right, 1: up, 2: down, 3: left


    foodmade = False
    running = True
    while running:
        win.border()

        while not foodmade:
            x, y = random.randrange(1, max_x - 1), random.randrange(1, max_y - 1)
            if win.inch(y, x) == ord(' '):
                foodmade = True
                win.addch(y, x, ord('@'))

        if deadcell not in body:
            win.addch(deadcell[0], deadcell[1], ' ')
        win.addch(head[0], head[1], 'X')

        # Bat phim nhap vao va ghi vao key
        key = win.getch()

        # Neu nhan q thi se thoat khoi vong lap
        if key == ord('q'):
            running == False

        # Bat su kien nhan phim di chuyen
        if key == curses.KEY_RIGHT and direction != 3:
            direction = 0
        elif key == curses.KEY_UP and direction != 2:
            direction = 1
        elif key == curses.KEY_DOWN and direction != 1:
            direction = 2
        elif key == curses.KEY_LEFT and direction != 0:
            direction = 3

        # Tang vi tri dau con ran len phia truoc
        if direction == 0:
            head[1] += 1
        elif direction == 1:
            head[0] -= 1
        elif direction == 2:
            head[0] += 1
        elif direction == 3:
            head[1] -= 1
        # Luc nay dau con ran van chua len toi truoc 

        # Kiem tra xem phia truoc co ky tu gi hay k
        # Nếu có thì con rắn đã chạm biên or vào thân or thức ăn
        if win.inch(head[0], head[1]) != ord(' '):
            if win.inch(head[0], head[1]) == ord('@'):
                foodmade = False
                body.append(body[-1])
            else:
                running = False
        
        deadcell = body[-1][:]
        for i in range(len(body) - 1, 0, -1):
            body[i] = body[i - 1][:]
        body[0] = head[:]
        


        win.refresh()
        time.sleep(0.1)

    win.clear()
    win.nodelay(0)
    message1 = 'Game Over'
    message2 = 'You got ' + str(len(body) - 5) + ' points'
    message3 = 'Press Space to play again'
    message4 = 'Press Enter to quit'
    win.addstr(int(max_y/2) - 1, int((max_x - len(message1))/2), message1)
    win.addstr(int(max_y/2), int((max_x - len(message2))/2), message2)
    win.addstr(int(max_y/2) + 1, int((max_x - len(message3))/2), message3)
    win.addstr(int(max_y/2) + 2, int((max_x - len(message4))/2), message4)
    win.refresh()
    q = 0
    while q not in [32, 10]:
        q = win.getch()
    if q == 32:
        win.clear()
        game()
    elif q == 10:
        curses.endwin()
        
if __name__ == '__main__':
    game()