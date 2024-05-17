from datetime import datetime
from decimal import Decimal
from pydantic.v1 import BaseSettings
from pydantic import BaseModel


class Settings(BaseSettings):
    arbitrary_types_allowed = True


class User(BaseModel):
    user_id: int
    username: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    is_admin: bool = False


class Product(BaseModel):
    product_id: int
    name: str
    description: str = None
    price: Decimal
    category_id: int


class Category(BaseModel):
    category_id: int
    name: str


class Order(BaseModel):
    order_id: int
    user_id: int
    order_date: datetime
    total_amount: Decimal
    product_order: int
