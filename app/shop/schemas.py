from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, time

# Category Schema
class CategorySchema(BaseModel):
    category_id: int
    category_name: str

    class Config:
        orm_mode = True


# Storage Schema
class StorageSchema(BaseModel):
    storage_id: int
    storage_address: str
    quantity: int

    class Config:
        orm_mode = True


# Product Schema
class ProductSchema(BaseModel):
    product_id: int
    product_name: str
    description: Optional[str] = None
    price: float
    color: Optional[str] = None
    weight: Optional[float] = None
    category_id: Optional[int] = None
    storage_id: Optional[int] = None

    class Config:
        orm_mode = True


# Customer Schema
class CustomerSchema(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    registration_date: datetime

    class Config:
        orm_mode = True


# Order Status Schema
class OrderStatusSchema(BaseModel):
    status_id: int
    status_description: str

    class Config:
        orm_mode = True


# Order Schema
class OrderSchema(BaseModel):
    order_id: int
    customer_id: int
    order_date: datetime
    total_amount: float
    status_id: int

    class Config:
        orm_mode = True


# Payment Schema
class PaymentSchema(BaseModel):
    payment_id: int
    order_id: int
    payment_method: str
    payment_amount: float
    payment_date: datetime

    class Config:
        orm_mode = True


# Shipping Schema
class ShippingSchema(BaseModel):
    shipping_id: int
    order_id: int
    shipping_address: str
    shipping_method: str
    shipping_cost: float
    shipping_date: datetime
    shipping_time: time

    class Config:
        orm_mode = True


# Order Item Schema
class OrderItemSchema(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True


# Review Schema
class ReviewSchema(BaseModel):
    review_id: int
    product_id: int
    customer_id: int
    review_text: Optional[str] = None
    rating: int
    review_date: datetime

    class Config:
        orm_mode = True


# Discount Schema
class DiscountSchema(BaseModel):
    promotion_id: int
    product_id: int
    discount_percent: float
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True
