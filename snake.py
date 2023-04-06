from turtle import Turtle
POSITION = [(0,0),(-20,0),(-40,0)]
SNAKE = []
class Snake:
    def __init__(self) -> None:
        pass

    def new_block(self,position):
        new_segment = Turtle()
        new_segment.pu()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        SNAKE.append(new_segment)

    def new_snake(self):
        for i in POSITION:
            self.new_block(i)
    def extend(self):
        self.new_block(SNAKE[-1].position())
    def move(self):
        for i in SNAKE:
            i.fd(50)
