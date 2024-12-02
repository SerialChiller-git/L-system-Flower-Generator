import turtle
from pygame import mixer
import random

mixer.init()


interations = 6
angle = 25.0

base = "X"
rules = {
    "X" : " F+[[X]-X]-F[-FX]+X",
    "F" : "FF"
}

def gen():
    string = base
    for i in range(interations):
        new_string = ""
        for j in string:
            new_string+= rules.get(j,j)
        string = new_string
    return string
    

def draw(t, instructions, length, angle):
    stack = []
    
    for i in (instructions):
        if i == 'F':
            t.forward(length)
        elif i == '-':
            flowers = random.randint(1,21)
            if(flowers == 7 or flowers == 21):
                t.dot(4, 'pink')
            t.right(angle)
        elif i == '+':
            flowers = random.randint(1,21)
            if(flowers == 7 or flowers == 21):
                t.dot(4, 'pink')
            t.left(angle)
            
        elif i == '[':
            stack.append((t.position(), t.heading()))
        elif i == ']':
            position , heading = stack.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()


def main():
    mixer.music.load("Digital Evolution.mp3") 
    mixer.music.play(-1) 
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Fractal Plant")

    t = turtle.Turtle()
    t.color('green')
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-150, -250)  
    t.pendown()
    t.left(90)  
    t.seth(45)
    command_string = gen()
    draw(t, command_string, 4.8, angle)

    screen.mainloop()

if __name__ == "__main__":
    main()
