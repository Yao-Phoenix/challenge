from base import Base
from sqlalchemy import Integer, Column, String

class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=True)
    city = Column(String(64), nullable=True)
    salary_lower = Column(Integer, nullable=True)
    salary_upper = Column(Integer, nullable=True)
    experience_lower = Column(Integer, nullable=True)
    experience_upper = Column(Integer, nullable=True)
    education = Column(String(16), nullable=True)
    tags = Column(String(256), nullable=True)
    company = Column(String(32), nullable=True)

if __name__ == '__main__':
    Base.metadata.create_all()
