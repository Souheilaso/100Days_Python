from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["question"]
    answer = item["correct_answer"]
    new_question = Question(text=question_text, answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Completed The Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
