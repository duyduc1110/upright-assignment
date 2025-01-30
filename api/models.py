from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sgd(Base):
    __tablename__ = 'sgds'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class FoodCategory(Base):
    __tablename__ = 'food_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Food(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    food_category_id = Column(Integer, ForeignKey('food_categories.id'), nullable=False)
    sgd_id = Column(Integer, ForeignKey('sgds.id'), nullable=False)

    food_category = relationship('FoodCategory')
    sgd = relationship('Sgd')

class CompanyRevenue(Base):
    __tablename__ = 'company_revenue'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    food_id = Column(Integer, ForeignKey('foods.id'), nullable=False)
    gmv = Column(Float, nullable=False)

    food = relationship('Food')