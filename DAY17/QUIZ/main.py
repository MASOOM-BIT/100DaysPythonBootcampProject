from question_model import Questions
from data import question_data

question_bank = []
for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    new_question = Questions(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank[0].answer)