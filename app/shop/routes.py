from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.shop import crud
from app.shop.schemas import (
    ProductSchema,
    CategorySchema,
    StorageSchema,
    ProductSchema,
    CustomerSchema,
    OrderSchema,
    OrderStatusSchema,
    PaymentSchema,
    ShippingSchema,
    OrderItemSchema,
    ReviewSchema,
    DiscountSchema,
)
from app.database import get_db  # Функция для получения сессии базы данных

router = APIRouter()

# Получить все продукты
@router.get("/products", response_model=List[ProductSchema])
async def get_products(db: AsyncSession = Depends(get_db)):
    products = await crud.get_all_products(db)
    return products

# Создать новый продукт
@router.post("/products", response_model=ProductSchema)
async def create_product(product_data: ProductSchema, db: AsyncSession = Depends(get_db)):
    new_product = await crud.create_product(db, product_data)
    return new_product

# Удалить продукт по ID
@router.delete("/products/{product_id}", response_model=bool)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_product(db, product_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return is_deleted

# 1. Получить все категории
@router.get("/categories", response_model=List[CategorySchema])
async def get_categories(db: AsyncSession = Depends(get_db)):
    categories = await crud.get_all_categories(db)
    return categories

# 2. Создать категорию
@router.post("/categories", response_model=CategorySchema)
async def create_category(category_data: CategorySchema, db: AsyncSession = Depends(get_db)):
    new_category = await crud.create_category(db, category_data)
    return new_category

# 3. Удалить категорию
@router.delete("/categories/{category_id}", response_model=bool)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_category(db, category_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return is_deleted


# 4. Получить все склады
@router.get("/storages", response_model=List[StorageSchema])
async def get_storages(db: AsyncSession = Depends(get_db)):
    storages = await crud.get_all_storages(db)
    return storages

# 5. Создать склад
@router.post("/storages", response_model=StorageSchema)
async def create_storage(storage_data: StorageSchema, db: AsyncSession = Depends(get_db)):
    new_storage = await crud.create_storage(db, storage_data)
    return new_storage

# 6. Удалить склад
@router.delete("/storages/{storage_id}", response_model=bool)
async def delete_storage(storage_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_storage(db, storage_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Storage not found")
    return is_deleted


# 7. Получить всех клиентов
@router.get("/customers", response_model=List[CustomerSchema])
async def get_customers(db: AsyncSession = Depends(get_db)):
    customers = await crud.get_all_customers(db)
    return customers

# 8. Создать клиента
@router.post("/customers", response_model=CustomerSchema)
async def create_customer(customer_data: CustomerSchema, db: AsyncSession = Depends(get_db)):
    new_customer = await crud.create_customer(db, customer_data)
    return new_customer

# 9. Удалить клиента
@router.delete("/customers/{customer_id}", response_model=bool)
async def delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_customer(db, customer_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return is_deleted


# 10. Получить все заказы
@router.get("/orders", response_model=List[OrderSchema])
async def get_orders(db: AsyncSession = Depends(get_db)):
    orders = await crud.get_all_orders(db)
    return orders

# 11. Создать заказ
@router.post("/orders", response_model=OrderSchema)
async def create_order(order_data: OrderSchema, db: AsyncSession = Depends(get_db)):
    new_order = await crud.create_order(db, order_data)
    return new_order

# 12. Удалить заказ
@router.delete("/orders/{order_id}", response_model=bool)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_order(db, order_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return is_deleted


# 13. Получить все статусы заказов
@router.get("/order-statuses", response_model=List[OrderStatusSchema])
async def get_order_statuses(db: AsyncSession = Depends(get_db)):
    statuses = await crud.get_all_order_statuses(db)
    return statuses

# 14. Создать статус заказа
@router.post("/order-statuses", response_model=OrderStatusSchema)
async def create_order_status(status_data: OrderStatusSchema, db: AsyncSession = Depends(get_db)):
    new_status = await crud.create_order_status(db, status_data)
    return new_status

# 15. Удалить статус заказа
@router.delete("/order-statuses/{status_id}", response_model=bool)
async def delete_order_status(status_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_order_status(db, status_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Order status not found")
    return is_deleted


# 16. Получить все платежи
@router.get("/payments", response_model=List[PaymentSchema])
async def get_payments(db: AsyncSession = Depends(get_db)):
    payments = await crud.get_all_payments(db)
    return payments

# 17. Создать платеж
@router.post("/payments", response_model=PaymentSchema)
async def create_payment(payment_data: PaymentSchema, db: AsyncSession = Depends(get_db)):
    new_payment = await crud.create_payment(db, payment_data)
    return new_payment

# 18. Удалить платеж
@router.delete("/payments/{payment_id}", response_model=bool)
async def delete_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_payment(db, payment_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Payment not found")
    return is_deleted


# 19. Получить все доставки
@router.get("/shipping", response_model=List[ShippingSchema])
async def get_shipping(db: AsyncSession = Depends(get_db)):
    shipping = await crud.get_all_shipping(db)
    return shipping

# 20. Создать доставку
@router.post("/shipping", response_model=ShippingSchema)
async def create_shipping(shipping_data: ShippingSchema, db: AsyncSession = Depends(get_db)):
    new_shipping = await crud.create_shipping(db, shipping_data)
    return new_shipping

# 21. Удалить доставку
@router.delete("/shipping/{shipping_id}", response_model=bool)
async def delete_shipping(shipping_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_shipping(db, shipping_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Shipping not found")
    return is_deleted


# 22. Получить все товары в заказах (order items)
@router.get("/order-items", response_model=List[OrderItemSchema])
async def get_order_items(db: AsyncSession = Depends(get_db)):
    order_items = await crud.get_all_order_items(db)
    return order_items

# 23. Создать товар в заказе
@router.post("/order-items", response_model=OrderItemSchema)
async def create_order_item(order_item_data: OrderItemSchema, db: AsyncSession = Depends(get_db)):
    new_order_item = await crud.create_order_item(db, order_item_data)
    return new_order_item

# 24. Удалить товар в заказе
@router.delete("/order-items/{order_item_id}", response_model=bool)
async def delete_order_item(order_item_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_order_item(db, order_item_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Order item not found")
    return is_deleted


# 25. Получить все отзывы
@router.get("/reviews", response_model=List[ReviewSchema])
async def get_reviews(db: AsyncSession = Depends(get_db)):
    reviews = await crud.get_all_reviews(db)
    return reviews

# 26. Создать отзыв
@router.post("/reviews", response_model=ReviewSchema)
async def create_review(review_data: ReviewSchema, db: AsyncSession = Depends(get_db)):
    new_review = await crud.create_review(db, review_data)
    return new_review

# 27. Удалить отзыв
@router.delete("/reviews/{review_id}", response_model=bool)
async def delete_review(review_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_review(db, review_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Review not found")
    return is_deleted


# 28. Получить все скидки
@router.get("/discounts", response_model=List[DiscountSchema])
async def get_discounts(db: AsyncSession = Depends(get_db)):
    discounts = await crud.get_all_discounts(db)
    return discounts

# 29. Создать скидку
@router.post("/discounts", response_model=DiscountSchema)
async def create_discount(discount_data: DiscountSchema, db: AsyncSession = Depends(get_db)):
    new_discount = await crud.create_discount(db, discount_data)
    return new_discount

# 30. Удалить скидку
@router.delete("/discounts/{promotion_id}", response_model=bool)
async def delete_discount(promotion_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await crud.delete_discount(db, promotion_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Discount not found")
    return is_deleted
