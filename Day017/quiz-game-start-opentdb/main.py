from data import Data
from quiz_brain import QuizBrain


def play_quiz():
    print("*** Welcome to Trivia Game ***")

    question_data = Data()

    quiz = QuizBrain(question_data.generate_questions())

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{len(quiz.questions_list)}")


play_quiz()
