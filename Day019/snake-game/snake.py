from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.snake_head = self.snakebody[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(MOVE_DISTANCE*(-i), 0)
            self.snakebody.append(new_segment)

    def move_forward(self):
        for seg_num in range(len(self.snakebody) - 1, 0, -1):
            self.snakebody[seg_num].goto(self.snakebody[seg_num - 1].position())
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)


if __name__ == "__main__":
    print("Snake module")