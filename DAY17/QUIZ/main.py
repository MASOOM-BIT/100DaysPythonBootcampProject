from question_model import Questions
from data import question_data
from quiz_brain import  QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions['question']
    question_answer = questions['correct_answer']
    new_question = Questions(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f'Your funal score was {quiz.score}/{quiz.question_number}')