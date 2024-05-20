from sqlalchemy import Column, String, Integer

from src.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
