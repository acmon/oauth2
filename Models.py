from pydantic import BaseModel


class Orders(BaseModel):
    user: str
    order: float
    previous_order: bool
