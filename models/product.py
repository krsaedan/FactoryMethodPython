from pydantic import BaseModel, Field
from models.pyObjectId import PyObjectId
from bson import ObjectId
from typing import Optional

class Product(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    price: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Product1",
                "price": "1000"
            }
        }