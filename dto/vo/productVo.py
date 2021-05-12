from typing import Optional
from pydantic import BaseModel

class ProductVo(BaseModel):
    id: Optional[str]
    name: str
    price: str