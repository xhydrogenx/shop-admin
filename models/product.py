from sqlalchemy import Column, String, Integer, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)

    category = relationship("Category", backref="products")
