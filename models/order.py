from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    product_order = Column(Integer, ForeignKey("products.product_id"), nullable=False)

    user = relationship("User", backref="orders")
    product = relationship("Product")
