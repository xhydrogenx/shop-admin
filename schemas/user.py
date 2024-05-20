from pydantic import BaseModel


class SUser(BaseModel):
    user_id: int
    username: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    is_admin: bool = False
