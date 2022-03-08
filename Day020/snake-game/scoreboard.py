from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
GAME_BOUNDARY = 290


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def keep_score(self, snake, food):
        # Detect collision with food
        if snake.snake_head.distance(food) < 15:
            self.score += 1
            food.refresh_food()
            snake.extend_snakebody()
            self.clear()
            self.update_scoreboard()

    def is_game_over(self, snake):
        # Detect collision with wall
        if -GAME_BOUNDARY < snake.snake_head.xcor() < GAME_BOUNDARY \
                and -GAME_BOUNDARY < snake.snake_head.ycor() < GAME_BOUNDARY:
            return False
        else:
            self.goto(0, 0)
            self.write("GAME OVER", align=ALIGNMENT, font=FONT)
            return True

        # Detect collision with tail
        # if head collides with any segment in the tail
        for segment in snake.snakebody[1:]:
            if snake.snake_head.distance(segment) < 10:
                self.goto(0, 0)
                self.write("GAME OVER", align=ALIGNMENT, font=FONT)
                return True

        return False

