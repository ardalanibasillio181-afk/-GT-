from sqlalchemy import Column, Integer, String, create_enginefrom sqlalchemy.ext.declarative import declarative_baseengine = create_engine('sqlite:///ecommerce.db')Base = declarative_base()
class Product(Base):tablename = 'products'id = Column(Integer, primary_key=True)name = Column(String)price = Column(Integer)
