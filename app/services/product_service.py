from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import product_repository
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, product: ProductCreate):
    return product_repository.create(db, product)


def list_products(db: Session):
    return product_repository.get_all(db)


def get_product(db: Session, product_id: int):
    product = product_repository.get_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    updated = product_repository.update(db, product_id, product)
    if updated is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated


def delete_product(db: Session, product_id: int):
    deleted = product_repository.delete(db, product_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}