import turtle as t
import random
timmy = t.Turtle()
screen = t.Screen()
screen.bgcolor('black')
timmy.shape('turtle')
t.colormode(255)
timmy.speed(2000)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor

for i in range(360):
    timmy.color(random_color())
    timmy.circle(200)
    timmy.setheading(timmy.heading()+10)






screen.exitonclick()
