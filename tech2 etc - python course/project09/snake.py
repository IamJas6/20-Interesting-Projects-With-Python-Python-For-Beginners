import turtle
import random
import time

#creating the screen
screen=turtle.Screen()
screen.title("THE SNAKE GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#creating border into the screen
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.color("blue")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score board
score=0
delay=0.1

#creating snake object
snake=turtle.Turtle()
snake.speed()
snake.shape("circle")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction='stop'

#creating food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(30, 30)

oldfood=[]

#creating score
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("red")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: ",align="center",font=("courier",24,"bold"))

#creating snake movement
def snake_up():
    if snake.direction!="down":
        snake.direction="up"
def snake_down():
    if snake.direction!="up":
        snake.direction="down"
def snake_left():
    if snake.direction!="right":
        snake.direction="left"
def snake_right():
    if snake.direction!="left":
        snake.direction="right"

def movement():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

#binding keyboard functions
screen.listen()
screen.onkeypress(snake_up,"Up")
screen.onkeypress(snake_down,"Down")
screen.onkeypress(snake_left,"Left")
screen.onkeypress(snake_right,"Right")

#main looop
while True:
    screen.update()

    #coliding snake and food
    if snake.distance(food)<20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        food.goto(x, y)
        scoring.clear()
        score=score+1
        scoring.write("Score: {}".format(score),align="center",font=("courier",24,"bold"))
        delay=delay-0.001

        #creating alternate or new food
        newfood=turtle.Turtle()
        newfood.speed(0)
        newfood.shape("circle")
        newfood.color("green")
        newfood.penup()
        oldfood.append(newfood)

    #adding ball to snake
    for index in range(len(oldfood) - 1, 0, -1):
        a=oldfood[index - 1].xcor()
        b=oldfood[index - 1].ycor()
        oldfood[index].goto(a, b)

    if len(oldfood)>0:
        a=snake.xcor()
        b=snake.ycor()
        oldfood[0].goto(a,b)
    movement()

    #border colision
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("cyan")
        scoring.goto(0,0)
        scoring.write("--------GAME OVER-------\n Your Score is {}".format(score),align="center",font=("courier",35,"bold"))

    #self coliding
    for food in oldfood:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("cyan")
            scoring.goto(0, 0)
            scoring.write("--------GAME OVER-------\n Your Score is {}".format(score), align="center",font=("courier", 35, "bold"))

    time.sleep(delay)
turtle.Terminator()