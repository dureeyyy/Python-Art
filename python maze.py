from turtle import *
import random

setup(1000, 1000)

def tiling(x, y, size, level, mode):
    if level == 0:
        if mode == 0:
            if random.random() < 0.5:
                # Vertical line
                penup()
                goto(x, y - size)
                pendown()
                goto(x, y + size)
            else:
                # Horizontal line
                penup()
                goto(x - size, y + size)
                pendown()
                goto(x + size, y - size)
        else:
            if random.random() < 0.5:
                # diagonal line
                penup()
                goto(x - size, y + size)
                pendown()
                goto(x + size, y - size)
            else:
                # diagonal line
                penup()
                goto(x - size, y - size)
                pendown()
                goto(x + size, y + size)        
    else:
        size /= 2
        level -= 1
        tiling(x + size, y + size, size, level, mode)
        tiling(x - size, y + size, size, level, mode)
        tiling(x - size, y - size, size, level, mode)
        tiling(x + size, y - size, size, level, mode)


def modeGenerator():
    # 0 for straight
    # 1 for diagonal
    value = random.randint(0, 1)
    return value


hideturtle()
tracer(False)     
tiling(0, 0, 400, 6, modeGenerator())
tracer(True)
exitonclick()