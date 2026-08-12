#table (jadval) besazim
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base #az database.py improt mikonim BASE


'''
yadavari
----USERS----
id  | name | answers |

'''
class User(Base):
    __tablename__ = 'users' #harchi bekhay mitoni bzri
    #columns --> esme id bashe , integer --> adade sahih
    #primary_key --> khod b khod besaze id , index bshe
    id = Column(Integer, primary_key=True, index=True)
    #--soton haye bade
    name = Column(String, nullable=False) #null khali bashe
    #answers = Column(String, nullable=False) #null khali bashe
    answer = relationship('Answers', back_populates='user')


#khalis akhtid 
'''
Questions --> table esh ro besazim
'''
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    #choices = Column(String, nullable=False)
    #answer = Column(Integer, nullable=False)
    choice = relationship('Choice', back_populates='question')
    answer = relationship('Answers', back_populates='question')




class Choice(Base):
    __tablename__  ='choice'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Questions', back_populates='choice')
    answer = relationship('Answers', back_populates='choice')


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_id = Column(Integer, ForeignKey('choice.id'))

    user = relationship('User', back_populates='answer')
    question = relationship('Questions', back_populates='answer')
    choice = relationship('Choice', back_populates='answer')
