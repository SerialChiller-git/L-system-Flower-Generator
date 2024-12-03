import turtle
from pygame import mixer
import random

mixer.init()


interations = 10
angle = 25.0

base = "X"
rules = {
    "X": [
        {"rule": "F[+X][-X]FX", "prob": 15},
        {"rule": "F[+X]F[-X]+X", "prob": 10},
        {"rule": "F[+X][-FX]F", "prob": 10},
        {"rule": "F[-X]F[+X]FX", "prob": 10},
        {"rule": "F[+X][-X][FX]", "prob": 5},
        {"rule": "F[+FX]-F[-FX]", "prob": 5},
        {"rule": "F[-FX]+F[+FX]", "prob": 5},
        {"rule": "F[-FX][-X][+FX]", "prob": 5},
        {"rule": "[+F[-X]][-F[+X]]", "prob": 5},
        {"rule": "F[+X]F[-X]F", "prob": 5},
        {"rule": "FF[+X]F[-X]X", "prob": 5},
        {"rule": "F[+X][-X]FXF", "prob": 5},
        {"rule": "F[+X][FX][-X]", "prob": 5},
        {"rule": "F[+FX][-FX]FX", "prob": 5}
    ],
    "F": [
        {"rule": "FF", "prob": 20},
        {"rule": "FFF", "prob": 5},
        {"rule": "F[+F]F[-F]", "prob": 20},
        {"rule": "F[-F][+F]", "prob": 15},
        {"rule": "[FF][+F][-F]", "prob": 15},
        {"rule": "F[-F][+F]F", "prob": 10},
        {"rule": "F[+FF][-FF][F]", "prob": 10},
        {"rule": "F[-FF][+FF]FF", "prob": 5}
    ]
}


def gen():
    string = base
    for i in range(interations):
        new_string = ""
        for j in string:
            new_string+= getOne(rules, j)
        string = new_string
    return string
    
def getOne(rules, char):
    if char not in rules:  
        return char

    choices = rules[char]
    
    cumulative = 0
    for choice in choices:
        rnd = random.randint(0, 100)
        if rnd <= choice["prob"]:
            return choice["rule"]
    return char  


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
    t.goto(0, -250)  
    t.pendown()
    t.left(90)  
    command_string = gen()
    draw(t, command_string, 4.8, angle)

    screen.mainloop()

if __name__ == "__main__":
    main()
