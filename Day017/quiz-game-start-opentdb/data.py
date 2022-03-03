import html
import requests
import random
from question_model import Question

# https://docs.python-requests.org/en/latest/user/install/
# https://opentdb.com/api_config.php
class Data:

    def __init__(self):
        self.question_data = []

    def prompt_user_for_number(self):
        num_of_questions = int(input("How many questions do you want to play? "))
        return num_of_questions

    def generate_questions(self):
        amount = self.prompt_user_for_number()
        category = random.choice(
            [9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
        url_string = f"https://opentdb.com/api.php?amount={amount}&category={category}&type=boolean"

        response = requests.get(url_string).json()
        for q in response["results"]:
            question = html.unescape(q["question"])
            self.question_data.append(Question(question, q["correct_answer"]))

        return self.question_data
