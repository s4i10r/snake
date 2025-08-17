"""Snake but its a Python"""

import os
import time

# CONTANTS
WIDTH = 30
HEIGHT = 10

# this list contains the snakes position
# start position
snake = [[HEIGHT//2, WIDTH//2+i] for i in range(5)]

# BASIC FIELD GENERATION AND DICT CREATION
field = [["." for i in range(WIDTH)] for i in range(HEIGHT)]




for i in range(100):
    # wipe screen for update
    os.system("cls" if os.name == "nt" else "clear")

    # reset field
    for row in field:
        for i in range(len(row)):
            row[i] = "."

    
    # place snake
    for i in range(len(snake)):
        field[snake[i][0]][snake[i][1]] = "O"


    for row in field:
        print("".join(row))

    # reposition snake
    del snake[0]
    # append the last farthest position + 1 and mod for travelling through the edge
    snake.append([(snake[-1][0])%WIDTH, (snake[-1][1]+1)%WIDTH])

    time.sleep(0.5)
