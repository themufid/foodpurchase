
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class FoodItemSerializer(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
