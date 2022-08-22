#https://www.youtube.com/watch?v=M_npdRYD4K0

#curses - library to munipulate the screen within terminal

import curses
from random import randint

#setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0) #this sets up new window with lines, columns, and starting at 0 and 0.  y is first, x is second
win.keypad(1) #we want to use the keypad and arrow keys to play
curses.noecho()# we don't want to listen to other input or output keys from the keyboard
curses.curs_set(0) #hides our curser
win.border(0) #sets a border
win.nodelay(1) #we are not using another users input with this function

# snake and food
snake = [(4, 10), (4,9), (4,8)] # we want a list of tuples here cas its immutable, this is also our starting point for the snake
food = (10, 20) # starting point for food

# game logic below

score = 0

ESC = 27 #this should run as long as the user doesn't hit the esc key. key is 27
key = curses.KEY_RIGHT #starting by moving snake to the right




while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + '.') #this gives us our score w coordinates and str
    win.timeout(150 - (len(snake)) // 5 + (len(snake)) // 10 % 120) #this increases speed of snake based on len of snake, from github formula


    prev_key = key # this gets our new key
    event = win.getch() #waiting for the next user input with this var
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]: #this makes sure we are using the right keys
        key = prev_key #gets us back to prev key

    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) #append an extra * to snake

    if y == 0: break  #this sets snake length on both x and y
    if y == 19: break
    if x == 0: break
    if x == 59: break


    if snake[0] in snake[1:]: break #if snake runs over itself

    if snake[0] == food: #randomizes the new food
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = () #while true loop continues
        win.addch(food[0], food[1], '#')
    else:
        last = snake.pop() #returns last snake and moves it
        win.addch(last[0], last[1], ' ') #at the end of the tail we want to add a space
    
    # for c in snake:
    #     win.addch(c[0], c[1], '*') #this is giving us our snake on the y, and x coordinates, this is just to make sure our
    win.addch(food[0], food[1], '#')
    win.addch(snake[0][0], snake[0][1], '*')


curses.endwin() #this ends the game
print(f"Final score = {score}")

