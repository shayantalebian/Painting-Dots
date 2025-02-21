import turtle as t
import random as r

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

#REVIEW - 10 by 10 grid, the sizes are 20 and the space between is 50
def draw():
    setX = -250
    setY = -250
    tim.penup()
    tim.setx(setX)
    tim.sety(setY)
    tim.pendown()
    
    for x in range(10):
        for y in range(10):
            tim.color(r.choice(color_list))
            tim.dot(20)
            tim.penup()
            tim.forward(50)
            tim.pendown()
        
        if x < 9:
            tim.penup()
            tim.setx(setX)
            setY = setY + 50
            tim.sety(setY)
            tim.pendown()
        else:
            tim.hideturtle()
        
    
draw()
#TODO - Make the game close by clicking on the screen
screen = t.Screen()
screen.exitonclick()

#NOTE - This is the way that we get the color from the image using the colorgram library
# import colorgram as col

# rgb_colors = []
# colors = col.extract('image.jpg', 300)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)