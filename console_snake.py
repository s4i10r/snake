"""Snake but its a Python"""

import os
import time
import msvcrt   # Windows specific

# CONTANTS
WIDTH = 30
HEIGHT = 10

running = True
direction = "w"

# this list contains the snakes position
# also start position
snake = [[HEIGHT//2, WIDTH//2+i] for i in range(5)]



def gen_field(WIDTH: int, HEIGHT: int) -> list:
    """
    generates the snake field
    """
    # field generation
    field = list()

    for i in range(HEIGHT):
        if i == 0 or i == HEIGHT - 1:
            field.append(["-" for i in range(WIDTH)])
        else:
            row = ["|"] + [" " for i in range(WIDTH-2)] + ["|"]
            field.append(row)

    return field

field = gen_field(WIDTH, HEIGHT)


def calc_snake(snake: list, direction: str, width: int, height: int)-> list:
    """
    calculates the positioning of the snake based on
    the current snake + direction
    """
    del snake[0]

    match direction:
        # wasd - top/left/down/right
        case "d":
            # take the farthest position and extend it to the right
            snake.append([snake[-1][0], (snake[-1][1]+1%width)])
        case "a":
            snake.append([snake[-1][0], (snake[-1][1]-1%width)])
        case "w":
            snake.append([(snake[-1][0]-1%height), snake[-1][1]])
        case "s":
            snake.append([(snake[-1][0]+1)%height, snake[-1][1]])
    
    return snake


def repos_snake(snake: list, field: list) -> list:
    """
    handles the reposition logic
    """

    # place snake
    for i in range(len(snake)):
        field[snake[i][0]][snake[i][1]] = "o"

    return field


# MAIN LOOP

if __name__ == "__main__":

    while running:
        # wipe screen for update
        os.system("cls" if os.name == "nt" else "clear")

        # reset field
        field = gen_field(WIDTH, HEIGHT)

        
        field = repos_snake(snake, field)


        for row in field:
            print("".join(row))

        # reposition snake
        # del snake[0]
        # # append the last farthest position + 1 and mod for travelling through the edge
        # snake.append([(snake[-1][0])%WIDTH, (snake[-1][1]+1)%WIDTH])

        if msvcrt.kbhit():  # checks for keypress
            direction = msvcrt.getch().decode("utf-8")
            
        snake = calc_snake(snake, direction, WIDTH, HEIGHT)

        time.sleep(0.4)
