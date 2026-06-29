from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import product  # importante: para que cree la tabla
from app.routes.product_routes import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Inventario v1")

app.include_router(product_router)