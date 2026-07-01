from pydantic import BaseModel, Field, field_validator
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0, le=10000000)
    stock: int = Field(ge=0, le=10000)
    category: str = Field(min_length=3)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        name = value.strip()
        if not name:
            raise ValueError("El nombre no puede estar vacío ni contener solo espacios")
        if name.lower() in ["test", "prueba", "producto"]:
            raise ValueError("El nombre del producto no está permitido")
        return name


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    price: Optional[float] = Field(default=None, gt=0, le=10000000)
    stock: Optional[int] = Field(default=None, ge=0, le=10000)
    category: Optional[str] = Field(default=None, min_length=3)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: Optional[str]):
        if value is None:
            return value
        name = value.strip()
        if not name:
            raise ValueError("El nombre no puede estar vacío ni contener solo espacios")
        if name.lower() in ["test", "prueba", "producto"]:
            raise ValueError("El nombre del producto no está permitido")
        return name


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True