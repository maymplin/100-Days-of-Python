from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
GAME_BOUNDARY = 290


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.is_game_over = False
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def keep_score(self, snake, food):
        # Detect collision with food
        if snake.snake_head.distance(food) < 15:
            self.score += 1
            food.refresh_food()
            snake.extend_snakebody()
            self.update_scoreboard()

    def detect_collision(self, snake):
        # Detect collision with wall
        if not -GAME_BOUNDARY < snake.snake_head.xcor() < GAME_BOUNDARY \
                or not -GAME_BOUNDARY < snake.snake_head.ycor() < GAME_BOUNDARY:
            self.reset_game(snake)

        # Detect collision with tail
        # if head collides with any segment in the tail
        for segment in snake.snakebody[1:]:
            if snake.snake_head.distance(segment) < 10:
                self.reset_game(snake)

    def reset_game(self, snake):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.update_scoreboard()
        self.score = 0
        snake.reset()

    def end_game(self):
        self.is_game_over = True
