from turtle import Turtle, Screen, color, position, up
from time import sleep
from random import randint

scr = Screen()
scr.title("Snake Game BOIIIIII")
scr.setup(width=700,height=700)
scr.bgcolor("Black")

boundary = Turtle()
boundary.shape("square")
boundary.color("white")
boundary.pu()
boundary.speed("fast")
boundary.goto(-300,250)
boundary.pd()
boundary.fd(610)
boundary.right(90)
boundary.fd(580)
boundary.right(90)
boundary.fd(620)
boundary.right(90)
boundary.fd(580)


scr.tracer(-1)
positions = [(0,0),(-20,0),(-40,0),(-60,0),(-80,0)]
snake = []
for i in range (4):
    new_block = Turtle()
    new_block.pu()
    new_block.goto(positions[i])
    new_block.color("white")
    new_block.shape("square")
    snake.append(new_block)

scr.update()

food = Turtle()
food.pu()
food.hideturtle()
x_random_food = randint(-200,200)
x_random_food = x_random_food - x_random_food%20
y_random_food = randint(-200,200)
y_random_food = y_random_food - y_random_food%20

food.goto(x_random_food,y_random_food)

food.dot(10,"blue")

scoreboard = Turtle()
score = 0
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 270)
scoreboard.hideturtle()

def update_scoreboard():
        scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def update_scoreboard_selfbang():
        scoreboard.write(f"HIT YOURSELF", align="center", font=("Courier", 24, "normal"))


update_scoreboard()

def d_key_function():
    if snake[0].heading() == 90:
        snake[0].right(90)
    elif snake[0].heading() == 270:
        snake[0].left(90)

def a_key_function():
    if snake[0].heading() == 90:
        snake[0].left(90)
    elif snake[0].heading() == 270:
        snake[0].right(90)

def w_key_function():
    if snake[0].heading() == 0:
        snake[0].left(90)
    elif snake[0].heading() == 180:
        snake[0].right(90)

def s_key_function():
    if snake[0].heading() == 0:
        snake[0].right(90)
    elif snake[0].heading() == 180:
        snake[0].left(90)

scr.listen()
scr.onkey(d_key_function,"Right")
scr.onkey(a_key_function,"Left")
scr.onkey(w_key_function,"Up")
scr.onkey(s_key_function,"Down")

game_is_on = True
food_is_on = True

while food_is_on and game_is_on:
    
    positions_of_blocks = []
    for block in snake:
        positions_of_blocks.append(block.position())
    
    snake[0].fd(20)

    for block in range(1,len(snake)):
        # print(f"{snake[block].position()} to {positions_of_blocks[block-1]}")
        snake[block].goto(positions_of_blocks[block-1])
        

        if snake[block].position()[0] > 260 or snake[block].position()[0] < -260 or snake[block].position()[1] > 200 or snake[block].position()[1] < -280:
            game_is_on = False
    scr.update()
    sleep(0.1)

    print(f"{(int(snake[0].position()[0]),int(snake[0].position()[1]))} == {(x_random_food,y_random_food)}")

    if snake[0].distance(x_random_food,y_random_food) < 15 :

        score+=1
        scoreboard.clear()
        update_scoreboard()

        food.dot(10,"black")
        x_random_food = randint(-200,200)
        x_random_food = x_random_food - x_random_food%20
        y_random_food = randint(-200,200)
        y_random_food = y_random_food - y_random_food%20
        food.goto(x_random_food,y_random_food)

        food.dot(10,"blue")
        new_block = Turtle()
        new_block.pu()
        new_block.goto(positions[i])
        new_block.color("white")
        new_block.shape("square")

        snake.append(new_block)
    
    for each_block in positions_of_blocks:
        if snake[0].distance(each_block) < 10:
            game_is_on = False
            scoreboard.clear()
            update_scoreboard_selfbang()

scr.exitonclick()