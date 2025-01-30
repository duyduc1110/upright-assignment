from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

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

    @hybrid_property
    def possible_sgd_id(self):
        if self.sgd_id is not None:
            return self.sgd_id
        if self.parent is not None:
            return self.parent.possible_sgd_id
        return None

    @hybrid_property
    def possible_impact_id(self):
        if self.impact_id is not None:
            return self.impact_id
        if self.parent is not None:
            return self.parent.possible_impact_id
        return None

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Revenue(Base):
    __tablename__ = 'revenues'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    gmv = Column(Float, nullable=False)

    company = relationship('Company')
    product = relationship('Product')