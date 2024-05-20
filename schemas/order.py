from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class SOrder(BaseModel):
    order_id: int
    user_id: int
    order_date: datetime
    total_amount: Decimal
    product_order: int
