from datetime import datetime, date
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from app.database import Base

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(70), unique=True)
    hashed_password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    expenses: Mapped[List['Expense']] = relationship(back_populates='user')
    categories: Mapped[List['Category']] = relationship(back_populates='owner')

class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('user.id'), nullable=True)
    name: Mapped[str] = mapped_column(String(35))
    color: Mapped[str] = mapped_column(String(10))
    expenses: Mapped[List['Expense']] = relationship(back_populates='category')
    owner: Mapped[Optional['User']] = relationship(back_populates='categories')


class Expense(Base):
    __tablename__ = 'expenses'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    amount: Mapped[float] = mapped_column()
    description: Mapped[str] = mapped_column(String(120))
    spent_on: Mapped[date] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user: Mapped['User'] = relationship(back_populates='expenses')
    category: Mapped['Category'] = relationship(back_populates='expenses')