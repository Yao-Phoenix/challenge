from base import Base
from sqlalchemy import Column, String, Integer, Float

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    score = Column(Float, nullable=True)
    count = Column(Integer, nullable=True)
    consumption = Column(Integer, nullable=True)
    sort = Column(String(64), nullable=True)
    bussiness_district = Column(String(64), nullable=True)
    taste = Column(Float, nullable=True)
    environment = Column(Float, nullable=True)
    seivice = Column(Float, nullable=True)

if __name__ == '__main__':
    Base.metadata.create_all()
