from fastapi import FastAPI
from app.shop.routes import router as shop_router  # Импорт маршрутов для магазина

app = FastAPI()

@app.get("/", response_model=dict)
async def root():
    return {"message": "Hello, world!"}

# Подключение маршрутов из shop.routes
app.include_router(shop_router, prefix="/shop", tags=["shop"])
