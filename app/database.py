from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///finance_tracker.db", echo=True)

Session = sessionmaker(engine)