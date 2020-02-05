from base import Base
from sqlalchemy import Column, String, Integer

class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    plot = Column(String(64), nullable=True)
    type = Column(String(64), nullable=True)
    area = Column(Integer, nullable=True)
    rent = Column(Integer, nullable=True)

if __name__ == '__main__':
    Base.metadata.create_all()
