from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DECIMAL,
    TIMESTAMP,
    Time,
    Text,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base


# Таблица categories
class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)


# Таблица storage
class Storage(Base):
    __tablename__ = "storage"

    storage_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    storage_address: Mapped[str] = mapped_column(String(200), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)


# Таблица products
class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    color: Mapped[str] = mapped_column(String(50), nullable=True)
    weight: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"), nullable=True)
    storage_id: Mapped[int] = mapped_column(ForeignKey("storage.storage_id"), nullable=True)

    category: Mapped["Category"] = relationship("Category", backref="products")
    storage: Mapped["Storage"] = relationship("Storage", backref="products")


# Таблица customers
class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    address: Mapped[str] = mapped_column(String(200), nullable=True)
    registration_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)


# Таблица order_statuses
class OrderStatus(Base):
    __tablename__ = "order_statuses"

    status_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status_description: Mapped[str] = mapped_column(String(100), nullable=False)


# Таблица orders
class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"), nullable=False)
    order_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)
    total_amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("order_statuses.status_id"), nullable=False)

    customer: Mapped["Customer"] = relationship("Customer", backref="orders")
    status: Mapped["OrderStatus"] = relationship("OrderStatus", backref="orders")


# Таблица payments
class Payment(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False, unique=True)
    payment_method: Mapped[str] = mapped_column(String(50), nullable=False)
    payment_amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    payment_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)

    order: Mapped["Order"] = relationship("Order", backref="payment")


# Таблица shipping
class Shipping(Base):
    __tablename__ = "shipping"

    shipping_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False, unique=True)
    shipping_address: Mapped[str] = mapped_column(String(200), nullable=False)
    shipping_method: Mapped[str] = mapped_column(String(50), nullable=False)
    shipping_cost: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    shipping_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)
    shipping_time: Mapped[str] = mapped_column(Time, nullable=False)

    order: Mapped["Order"] = relationship("Order", backref="shipping")


# Таблица order_items
class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)

    order: Mapped["Order"] = relationship("Order", backref="order_items")
    product: Mapped["Product"] = relationship("Product", backref="order_items")


# Таблица reviews
class Review(Base):
    __tablename__ = "reviews"

    review_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"), nullable=False)
    review_text: Mapped[str] = mapped_column(String(500), nullable=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)

    product: Mapped["Product"] = relationship("Product", backref="reviews")
    customer: Mapped["Customer"] = relationship("Customer", backref="reviews")


# Таблица discounts
class Discount(Base):
    __tablename__ = "discounts"

    promotion_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    discount_percent: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    start_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)
    end_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)

    product: Mapped["Product"] = relationship("Product", backref="discounts")
