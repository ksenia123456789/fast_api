from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import async_session_maker  # Фабрика для асинхронных сессий
from app.shop.models import Product  # Импорт модели продукта
from app.shop.schemas import ProductSchema  # Импорт схемы для сериализации

app = FastAPI()

@app.get("/", response_model=dict)
async def root():
    return {"message": "Hello, world!"}

# GET /products - возвращает список всех продуктов
@app.get("/products", response_model=list[ProductSchema])
async def get_products():
    async with async_session_maker() as session:  # Открываем асинхронную сессию
        result = await session.execute(select(Product))  # Выполняем SQL-запрос для всех продуктов
        products = result.scalars().all()  # Получаем список всех продуктов
    return products
