from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.snakebody = []
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(20 * (-i), 0)
            self.snakebody.append(new_segment)

    def move_forward(self):
        for seg_num in range(len(self.snakebody) - 1, 0, -1):
            self.snakebody[seg_num].goto(self.snakebody[seg_num - 1].position())
        self.snakebody[0].forward(20)


if __name__ == "__main__":
    print("Snake module")