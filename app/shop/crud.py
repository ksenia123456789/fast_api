from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.shop.models import (
    Product, Category, Storage, Customer, OrderStatus, Order, Payment,
    Shipping, OrderItem, Review, Discount
)
from app.shop.schemas import (
    ProductSchema, CategorySchema, StorageSchema, CustomerSchema,
    OrderStatusSchema, OrderSchema, PaymentSchema, ShippingSchema,
    OrderItemSchema, ReviewSchema, DiscountSchema
)

# --- Для Product ---
# Получить все продукты
async def get_all_products(db: AsyncSession):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


# Создать новый продукт
async def create_product(db: AsyncSession, product_data: ProductSchema):
    new_product = Product(
        product_name=product_data.product_name,
        description=product_data.description,
        price=product_data.price,
        color=product_data.color,  # Обязательно передаем color
        weight=product_data.weight,  # Обязательно передаем weight
        category_id=product_data.category_id,  # category_id передаем как есть
        storage_id=product_data.storage_id  # Если есть storage_id, передаем его
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)  # Обновляем объект, чтобы вернуть полную информацию
    return new_product



# Удалить продукт по ID
async def delete_product(db: AsyncSession, product_id: int):
    product = await db.get(Product, product_id)
    if product:
        await db.delete(product)
        await db.commit()
        return True



# --- Для Category ---
# Получить все категории
async def get_all_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    categories = result.scalars().all()
    return categories

# Создать новую категорию
async def create_category(db: AsyncSession, category_data: CategorySchema):
    new_category = Category(category_name=category_data.category_name)
    db.add(new_category)
    await db.commit()
    return new_category

# Удалить категорию по ID
async def delete_category(db: AsyncSession, category_id: int):
    category = await db.get(Category, category_id)
    if category:
        await db.delete(category)
        await db.commit()
        return True
    return False


# --- Для Storage ---
# Получить все склады
async def get_all_storages(db: AsyncSession):
    result = await db.execute(select(Storage))
    storages = result.scalars().all()
    return storages

# Создать новый склад
async def create_storage(db: AsyncSession, storage_data: StorageSchema):
    new_storage = Storage(
        storage_address=storage_data.storage_address,
        quantity=storage_data.quantity
    )
    db.add(new_storage)
    await db.commit()
    return new_storage

# Удалить склад по ID
async def delete_storage(db: AsyncSession, storage_id: int):
    storage = await db.get(Storage, storage_id)
    if storage:
        await db.delete(storage)
        await db.commit()
        return True
    return False


# --- Для Customer ---
# Получить всех клиентов
async def get_all_customers(db: AsyncSession):
    result = await db.execute(select(Customer))
    customers = result.scalars().all()
    return customers

# Создать нового клиента
async def create_customer(db: AsyncSession, customer_data: CustomerSchema):
    new_customer = Customer(
        first_name=customer_data.first_name,
        last_name=customer_data.last_name,
        email=customer_data.email,
        phone=customer_data.phone,
        address=customer_data.address,
        registration_date=customer_data.registration_date
    )
    db.add(new_customer)
    await db.commit()
    return new_customer

# Удалить клиента по ID
async def delete_customer(db: AsyncSession, customer_id: int):
    customer = await db.get(Customer, customer_id)
    if customer:
        await db.delete(customer)
        await db.commit()
        return True
    return False


# --- Для OrderStatus ---
# Получить все статусы заказов
async def get_all_order_statuses(db: AsyncSession):
    result = await db.execute(select(OrderStatus))
    statuses = result.scalars().all()
    return statuses

# Создать новый статус заказа
async def create_order_status(db: AsyncSession, status_data: OrderStatusSchema):
    new_status = OrderStatus(status_description=status_data.status_description)
    db.add(new_status)
    await db.commit()
    return new_status

# Удалить статус заказа по ID
async def delete_order_status(db: AsyncSession, status_id: int):
    status = await db.get(OrderStatus, status_id)
    if status:
        await db.delete(status)
        await db.commit()
        return True
    return False


# --- Для Order ---
# Получить все заказы
async def get_all_orders(db: AsyncSession):
    result = await db.execute(select(Order))
    orders = result.scalars().all()
    return orders

# Создать новый заказ
async def create_order(db: AsyncSession, order_data: OrderSchema):
    new_order = Order(
        customer_id=order_data.customer_id,
        order_date=order_data.order_date,
        total_amount=order_data.total_amount,
        status_id=order_data.status_id
    )
    db.add(new_order)
    await db.commit()
    return new_order

# Удалить заказ по ID
async def delete_order(db: AsyncSession, order_id: int):
    order = await db.get(Order, order_id)
    if order:
        await db.delete(order)
        await db.commit()
        return True
    return False


# --- Для Payment ---
# Получить все платежи
async def get_all_payments(db: AsyncSession):
    result = await db.execute(select(Payment))
    payments = result.scalars().all()
    return payments

# Создать новый платеж
async def create_payment(db: AsyncSession, payment_data: PaymentSchema):
    new_payment = Payment(
        order_id=payment_data.order_id,
        payment_method=payment_data.payment_method,
        payment_amount=payment_data.payment_amount,
        payment_date=payment_data.payment_date
    )
    db.add(new_payment)
    await db.commit()
    return new_payment

# Удалить платеж по ID
async def delete_payment(db: AsyncSession, payment_id: int):
    payment = await db.get(Payment, payment_id)
    if payment:
        await db.delete(payment)
        await db.commit()
        return True
    return False


# --- Для Shipping ---
# Получить все доставки
async def get_all_shippings(db: AsyncSession):
    result = await db.execute(select(Shipping))
    shippings = result.scalars().all()
    return shippings

# Создать новую доставку
async def create_shipping(db: AsyncSession, shipping_data: ShippingSchema):
    new_shipping = Shipping(
        order_id=shipping_data.order_id,
        shipping_address=shipping_data.shipping_address,
        shipping_method=shipping_data.shipping_method,
        shipping_cost=shipping_data.shipping_cost,
        shipping_date=shipping_data.shipping_date,
        shipping_time=shipping_data.shipping_time
    )
    db.add(new_shipping)
    await db.commit()
    return new_shipping

# Удалить доставку по ID
async def delete_shipping(db: AsyncSession, shipping_id: int):
    shipping = await db.get(Shipping, shipping_id)
    if shipping:
        await db.delete(shipping)
        await db.commit()
        return True
    return False


# --- Для OrderItem ---
# Получить все товары в заказах
async def get_all_order_items(db: AsyncSession):
    result = await db.execute(select(OrderItem))
    order_items = result.scalars().all()
    return order_items

# Создать новый товар в заказе
async def create_order_item(db: AsyncSession, order_item_data: OrderItemSchema):
    new_order_item = OrderItem(
        order_id=order_item_data.order_id,
        product_id=order_item_data.product_id,
        quantity=order_item_data.quantity,
        price=order_item_data.price
    )
    db.add(new_order_item)
    await db.commit()
    return new_order_item

# Удалить товар из заказа по ID
async def delete_order_item(db: AsyncSession, order_item_id: int):
    order_item = await db.get(OrderItem, order_item_id)
    if order_item:
        await db.delete(order_item)
        await db.commit()
        return True
    return False


# --- Для Review ---
# Получить все отзывы
async def get_all_reviews(db: AsyncSession):
    result = await db.execute(select(Review))
    reviews = result.scalars().all()
    return reviews

# Создать новый отзыв
async def create_review(db: AsyncSession, review_data: ReviewSchema):
    new_review = Review(
        product_id=review_data.product_id,
        customer_id=review_data.customer_id,
        review_text=review_data.review_text,
        rating=review_data.rating,
        review_date=review_data.review_date
    )
    db.add(new_review)
    await db.commit()
    return new_review

# Удалить отзыв по ID
async def delete_review(db: AsyncSession, review_id: int):
    review = await db.get(Review, review_id)
    if review:
        await db.delete(review)
        await db.commit()
        return True
    return False


# --- Для Discount ---
# Получить все скидки
async def get_all_discounts(db: AsyncSession):
    result = await db.execute(select(Discount))
    discounts = result.scalars().all()
    return discounts

# Создать новую скидку
async def create_discount(db: AsyncSession, discount_data: DiscountSchema):
    new_discount = Discount(
        product_id=discount_data.product_id,
        discount_percent=discount_data.discount_percent,
        start_date=discount_data.start_date,
        end_date=discount_data.end_date
    )
    db.add(new_discount)
    await db.commit()
    return new_discount

# Удалить скидку по ID
async def delete_discount(db: AsyncSession, promotion_id: int):
    discount = await db.get(Discount, promotion_id)
    if discount:
        await db.delete(discount)
        await db.commit()
        return True
    return False
