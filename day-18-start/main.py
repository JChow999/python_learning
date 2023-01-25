import turtle as franklin
import random


# import colorgram
#
#
# colors = colorgram.extract("garbage.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

rgb_colors = [(1, 13, 31), (52, 25, 16), (219, 127, 106), (9, 105, 160), (242, 213, 68), (149, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (10, 62, 31), (96, 6, 19), (206, 74, 104), (11, 96, 57), (0, 63, 145), (173, 135, 162), (7, 173, 216), (157, 34, 24), (4, 212, 207), (8, 140, 86), (145, 227, 216), (122, 193, 148), (101, 219, 229), (221, 178, 216), (252, 197, 0), (80, 135, 179)]

PACES = 50
XPOS = -220
YPOS = -250
DIMENSION = 10

franklin.hideturtle()
franklin.colormode(255)
franklin.penup()
franklin.speed(0)
franklin.setpos(XPOS,YPOS)

for x in range(DIMENSION):
    for num in range(DIMENSION):
        color = random.choice(rgb_colors)
        franklin.dot(20, color)
        franklin.forward(PACES)
    YPOS += 50
    franklin.setpos(XPOS, YPOS)



franklin.exitonclick()
