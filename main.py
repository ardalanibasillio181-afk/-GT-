from flask import Flask
app = Flask(name)
from database import engine
from models import Product
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
@app.route('/')
def index():
products = session.query (Product).all () 
return str (products)
