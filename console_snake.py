"""Snake but its a Python"""

import os
import time
import msvcrt   # Windows specific

# CONTANTS
WIDTH = 50
HEIGHT = 10

running = True
direction = "d"

# this list contains the snakes position
# also start position
# example: [[5, 15], [5, 16], [5, 17], [5, 18], [5, 19]]
snake = [[HEIGHT//2, WIDTH//2+i] for i in range(5)]
print(snake)


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
            snake.append([snake[-1][0], (snake[-1][1]+1)])
        case "a":
            snake.append([snake[-1][0], (snake[-1][1]-1)])
        case "w":
            snake.append([(snake[-1][0]-1), snake[-1][1]])
        case "s":
            snake.append([(snake[-1][0]+1), snake[-1][1]])
    
    return snake

def check_collision(snake: list, width: int, height: int) -> bool:
    """
    checks for collision
    """
    snakehead = snake[-1]   # which is a list of 2 numbers (coordinates)

    if snakehead[0] == 0 or snakehead[0] == height-1 or \
       snakehead[1] == 0 or snakehead[1] == width-1:
        return True
    else:
        return False
    


def draw_snake(snake: list, field: list) -> list:
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



        snake = calc_snake(snake, direction, WIDTH, HEIGHT)

        field = draw_snake(snake, field)
        
        for row in field:
            print("".join(row))

        if check_collision(snake, WIDTH, HEIGHT) == True:
            running = False


        if msvcrt.kbhit():  # checks for keypress
            direction = msvcrt.getch().decode("utf-8")
            

        time.sleep(0.3)


print("game over")