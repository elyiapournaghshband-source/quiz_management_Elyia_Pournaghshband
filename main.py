from database import Base, engine, get_db
from crud import create_user, create_question, add_choice, list_questions, submit_answer, calculate_score, reset_user_answers
from models import User, Questions, Choice, Answers

db = get_db()

print('==============Mini Quiz demo================')
print('first you must insert your name')

name = input('enter your name: ')
usr1 = create_user(db, name=name)

reset_user_answers(db, usr1.id)

questions = list_questions(db)

for q in questions:
    print(f'\nQuestion: {q.text}')
    
    choice_list = []
    for idx, c in enumerate(q.choice, 1):
        print(f'  {idx}. {c.text}')
        choice_list.append((idx, c.id))
    
    while True:
        try:
            user_choice = int(input('Enter the number of your choice (1-3): '))
            if 1 <= user_choice <= len(choice_list):
                break
            else:
                print(f"Please enter a number between 1 and {len(choice_list)}")
        except ValueError:
            print("Please enter a valid number.")
    
    chosen_db_id = None
    for display_num, db_id in choice_list:
        if display_num == user_choice:
            chosen_db_id = db_id
            break
    
    submit_answer(db, user_id=usr1.id, question_id=q.id, choice_id=chosen_db_id)

print('\n✅ All answers submitted!')

score = calculate_score(db, usr1.id)
max_score = len(questions) * 5

print(f'\n🎯 Your final score: {score} out of {max_score}')