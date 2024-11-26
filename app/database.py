from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from app.config import get_db_url  # Указываем путь до функции get_db_url

# Получение строки подключения
DATABASE_URL = get_db_url()

# Создание асинхронного движка и фабрики сессий
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Настройка аннотаций для моделей
int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=func.now())]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


# Базовый класс для моделей
class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"  # Таблицы будут названы автоматически, например, "products"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


# Функция для получения сессии базы данных
async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
