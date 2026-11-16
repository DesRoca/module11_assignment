from pydantic import BaseModel, model_validator
from typing import Literal
from uuid import UUID


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: Literal["add", "subtract", "multiply", "divide"]

    @model_validator(mode="after")
    def validate_division(self):
        if self.type == "divide" and self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self

class CalculationRead(CalculationCreate):
    id: int
    result: float
    user_id: UUID

    model_config = {"from_attributes": True}
    