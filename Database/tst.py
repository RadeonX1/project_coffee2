import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('postgresql://root:0946192332:3306/test') #11243 Database postgresSQL

Base = declarative_base()

class STUDENT(Base):
        __tablename__ = 'students'
        student_id = Column(String(13), primary_key = True ,nullable=True)
        f_name = Column(String(30),nullable=True)
        l_name = Column(String(30),nullable=True)
        e_mail = Column(String(50),nullable=True)

        def __repr__(self) :
                return '<User(student_id = {} , f_name = {} , l_name = {} , e_mail = {})>'.format(self.student_id,self.f_name,
                self.l_name,self.e_mail)
