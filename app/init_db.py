from app.database import Base, engine
from app.models import User, Category, Expense  # импорт нужен, чтобы Base "узнал" про эти таблицы

Base.metadata.create_all(bind=engine)