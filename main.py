import colorgram
colors = colorgram.extract('image.jpg', 25)
from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.speed("fastest")
# print(colors)
# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(193, 171, 124), (151, 99, 61), (10, 50, 73), (59, 30, 23), (181, 157, 54), (111, 71, 83), (124, 163, 176), (122, 37, 27), (34, 116, 160), (80, 134, 83), (12, 60, 42), (69, 31, 37), (76, 154, 125), (109, 40, 45), (210, 201, 148), (181, 100, 85), (141, 177, 161), (179, 152, 158), (178, 203, 183), (22, 76, 95), (221, 180, 169)]
screen.colormode(255)
tim.pu()
tim.hideturtle()
tim.setpos(-250,-250)
tim.showturtle()
tim.width(10)
tim.ht()


def row(num_of_dots):
    """Places inputed number of multicolor dots in a row"""
    for _ in range(num_of_dots):
        color = random.choice(color_list)
        tim.color(color)
        tim.dot(20)
        tim.penup()
        tim.forward(50)

def next_row():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(width * 50)
    tim.left(180)

width = 10
height = 10
for _ in range(height):
    row(width)
    next_row()





screen.exitonclick()