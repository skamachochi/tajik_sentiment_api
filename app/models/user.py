from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(64))
    username = mapped_column(String(64))
    hashed_password = mapped_column(String(64))
    created_at = mapped_column(DateTime, default=datetime.utcnow)
    is_active = mapped_column(Boolean, default=True)

class Prediction(Base):
    __tablename__ = "predictions"

    id = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    input_text = mapped_column(Text)
    label = mapped_column(String(64))
    confidence = mapped_column(Float)
    created_at = mapped_column(DateTime, default=datetime.utcnow)