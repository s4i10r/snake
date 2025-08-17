"""Snake but its a Python"""

import os
import time

# CONTANTS
WIDTH = 30
HEIGHT = 10

running = True


# this list contains the snakes position
# also start position
snake = [[HEIGHT//2, WIDTH//2+i] for i in range(5)]



def gen_field(WIDTH: int, HEIGHT: int) -> list:
    """
    generates the snake field
    """
    # BASIC FIELD GENERATION
    field = [["." for i in range(WIDTH)] for i in range(HEIGHT)]

    return field

field = gen_field(WIDTH, HEIGHT)



# alternative field generation
# alt_field = [[] for i in range(HEIGHT)] # TODO: hm

# for i in range(WIDTH):
#     alt_field[0].append("*")
#     alt_field[-1].append("*")


def repos_snake(snake: list, field: list) -> list:
    """
    handles the reposition logic
    """

    # place snake
    for i in range(len(snake)):
        field[snake[i][0]][snake[i][1]] = "O"

    return field


# MAIN LOOP

if __name__ == "__main__":

    while running:
        # wipe screen for update
        os.system("cls" if os.name == "nt" else "clear")

        # reset field
        for row in field:
            for i in range(len(row)):
                row[i] = "."

        
        field = repos_snake(snake, field)


        for row in field:
            print("".join(row))

        # reposition snake
        del snake[0]
        # append the last farthest position + 1 and mod for travelling through the edge
        snake.append([(snake[-1][0])%WIDTH, (snake[-1][1]+1)%WIDTH])

        time.sleep(0.5)
