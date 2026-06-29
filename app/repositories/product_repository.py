from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_all(db: Session):
    return db.query(Product).all()


def get_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_by_id(db, product_id)
    if db_product is None:
        return None
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete(db: Session, product_id: int):
    db_product = get_by_id(db, product_id)
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product