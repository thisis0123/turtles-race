from turtle import Turtle,Screen
import random

window=Screen()
window.setup(800,600)

turtles=[]
colors=("red","blue","green")
y_cors=(0,100,-100)

def create_turtles():
    for i in range(3):
        new_turtle=Turtle("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-380,y_cors[i])
        turtles.append(new_turtle)

def move_turtles():
    while True:
        if turtles[0].xcor()<380:
            turtles[0].forward(random.randint(1,5))
        else:
            return "red"
            
        if turtles[1].xcor()<380:
            turtles[1].forward(random.randint(1,5))
        else:
            return "blue"

        if turtles[2].xcor()<380:
            turtles[2].forward(random.randint(1,5))
        else:
            return "green"


create_turtles()
guessed_winner=window.textinput("who's the winner?","Guess who is gonna win?(red,blue,or green)").lower()
winner=move_turtles()

new_turtle=Turtle()
new_turtle.hideturtle()
new_turtle.pencolor("white")
new_turtle.penup()
window.bgcolor("black")   

if guessed_winner==winner: 
    new_turtle.write("Your guess is right\n",align="center",font=("Arial",20,"normal"))
    new_turtle.goto(0,-50)
    new_turtle.write("You win!\n",align="center",font=("Arial",20,"normal"))
else:
    new_turtle.write("Your guess is wrong\n",align="center",font=("Arial",20,"normal"))
    new_turtle.goto(0,-50)
    new_turtle.write("You lose!\n",align="center",font=("Arial",20,"normal"))






window.exitonclick()