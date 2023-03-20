"""Flask SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

# config = dotenv_values("config.env")
# Base = declarative_base()
# engine = create_engine(url = config["SQLALCHEMY_DATABASE_URI"])

# session_factory = sessionmaker(bind=engine)