from decimal import Decimal

from pydantic import BaseModel


class SProduct(BaseModel):
    product_id: int
    name: str
    description: str = None
    price: Decimal
    category_id: int
