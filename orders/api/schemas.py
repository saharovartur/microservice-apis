from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, conlist, conint, field_validator


class Size(Enum):
    small = "small"
    medium = "medium"
    big = "big"


class Status(Enum):
    created = "created"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1

    @field_validator("quantity")
    def quantity_non_nullable(cls, value):
        if value is None:
            raise ValueError("Количество не может быть равным нулю")
        return value


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]
