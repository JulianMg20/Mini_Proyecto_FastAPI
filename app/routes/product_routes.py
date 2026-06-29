from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)


@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_service.list_products(db)


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, product)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)