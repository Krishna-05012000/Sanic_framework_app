# models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    location = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
