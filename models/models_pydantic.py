from datetime import datetime
from decimal import Decimal
from pydantic.v1 import BaseSettings
from pydantic import BaseModel


class Settings(BaseSettings):
    arbitrary_types_allowed = True


class User(BaseModel):
    user_id: int  # ID пользователя (будет автоматически генерироваться)
    username: str  # Имя пользователя
    email: str  # Адрес электронной почты
    password_hash: str  # Хешированный пароль
    first_name: str  # Имя
    last_name: str  # Фамилия
    is_admin: bool = False  # Является ли администратором


class Product(BaseModel):
    product_id: int  # ID товара (будет автоматически генерироваться)
    name: str  # Название товара
    description: str = None  # Описание товара
    price: Decimal  # Цена товара
    category_id: int  # ID категории


class Category(BaseModel):
    category_id: int  # ID категории (будет автоматически генерироваться)
    name: str  # Название категории


class Order(BaseModel):
    order_id: int  # ID заказа (будет автоматически генерироваться)
    user_id: int  # ID пользователя
    order_date: datetime  # Дата заказа
    total_amount: Decimal  # Общая сумма заказа
    product_order: int





