from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories import product_repository
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, product: ProductCreate):
    existing = product_repository.get_by_name(db, product.name)
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "error": {
                    "code": "PRODUCT_ALREADY_EXISTS",
                    "message": "Ya existe un producto con ese nombre",
                }
            },
        )
    return product_repository.create(db, product)


def list_products(db: Session):
    return product_repository.get_all(db)


def get_product(db: Session, product_id: int):
    product = product_repository.get_by_id(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": {
                    "code": "PRODUCT_NOT_FOUND",
                    "message": "El producto solicitado no existe",
                }
            },
        )
    return product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    update_data = product.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": {
                    "code": "EMPTY_UPDATE_BODY",
                    "message": "Debe enviar al menos un campo para actualizar",
                }
            },
        )

    existing_product = product_repository.get_by_id(db, product_id)
    if existing_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": {
                    "code": "PRODUCT_NOT_FOUND",
                    "message": "El producto solicitado no existe",
                }
            },
        )

    new_name = update_data.get("name")
    if new_name is not None:
        product_with_same_name = product_repository.get_by_name(db, new_name)
        if product_with_same_name is not None and product_with_same_name.id != product_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "error": {
                        "code": "PRODUCT_ALREADY_EXISTS",
                        "message": "Ya existe un producto con ese nombre",
                    }
                },
            )

    return product_repository.update(db, product_id, product)


def delete_product(db: Session, product_id: int):
    deleted = product_repository.delete(db, product_id)
    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": {
                    "code": "PRODUCT_NOT_FOUND",
                    "message": "El producto solicitado no existe",
                }
            },
        )
    return {"mensaje": "Producto eliminado correctamente"}