from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sgd(Base):
    __tablename__ = 'sgds'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Impact(Base):
    __tablename__ = 'impacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sgd_id = Column(Integer, ForeignKey('sgds.id'), nullable=True)
    impact_id = Column(Integer, ForeignKey('impacts.id'), nullable=True)
    parent_id = Column(Integer, ForeignKey('products.id'), nullable=True)

    sgd = relationship('Sgd')
    impact = relationship('Impact')
    parent = relationship('Product', remote_side=[id], back_populates='children')
    children = relationship('Product', back_populates='parent')

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class CompanyRevenue(Base):
    __tablename__ = 'company_revenue'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    gmv = Column(Float, nullable=False)

    company = relationship('Company')
    product = relationship('Product')