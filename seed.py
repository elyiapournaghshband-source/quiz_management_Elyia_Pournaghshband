#seed.py --> jaee k shoam question haro tarahi mikonid

from database import Base, engine, get_db
from crud import create_user, create_question, add_choice, list_questions
from models import Questions, Choice

print('Creating tables...')
Base.metadata.create_all(engine)
print('Tables created successfully')

db = get_db()

# --- CLEANUP: Delete existing questions and choices to avoid duplicates ---
print('Cleaning up old data...')
db.query(Choice).delete()
db.query(Questions).delete()
db.commit()
print('Old data removed')

print('Creating questions...')

q1 = create_question(db, text='Is python a case-sensitive language?')
add_choice(db, q1, text='yes', is_correct=True)
add_choice(db, q1, text='no', is_correct=False)
add_choice(db, q1, text='maybe', is_correct=False)

q2 = create_question(db, text='When was Python created?')
add_choice(db, q2, text='1998', is_correct=False)
add_choice(db, q2, text='1985', is_correct=False)
add_choice(db, q2, text='1991', is_correct=True)

q3 = create_question(db, text='How many numeric data types does python have?')
add_choice(db, q3, text='5', is_correct=False)
add_choice(db, q3, text='3', is_correct=True)
add_choice(db, q3, text='7', is_correct=False)

q4 = create_question(db, text='Where is python headquarters?')
add_choice(db, q4, text='USA', is_correct=True)
add_choice(db, q4, text='Germany', is_correct=False)
add_choice(db, q4, text='Switzerland', is_correct=False)

print('Questions created successfully')
print('finalizing...')