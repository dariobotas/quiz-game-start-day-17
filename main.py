from question_model import Question
from data import question_data1, question_data2, question_data3, question_data4
from quiz_brain import QuizBrain
from random import randint

def build_questions_banks(list, key1, key2):
  question_bank = []
  for question in list:
    question_text = question[key1]
    question_answer = question[key2]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
  return question_bank
  
  
#question_bank = []
"""for question in question_data1:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

#question_bank1 = build_questions_banks(question_data1, "text", "answer")
#print(question_bank1[0].text)
#print(len(question_bank1))

#question_bank2 = build_questions_banks(question_data2, "question", "correct_answer")
#print(question_bank2[0].text)
#print(len(question_bank2))"""

data_from = randint(0,3)
question_data = [question_data1,question_data2,question_data3,question_data4]
print(f"{len(question_data[data_from])} questions")
question_bank = build_questions_banks(question_data[data_from],"question","correct_answer")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")