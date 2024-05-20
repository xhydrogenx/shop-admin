from pydantic import BaseModel


class SCategory(BaseModel):
    category_id: int
    name: str
