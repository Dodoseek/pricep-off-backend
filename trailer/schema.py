from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, field_serializer

from enum import Enum

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.trailer.trailer import Trailer


class TrailerStatus(str, Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    UNAVAILABLE = "unavailable"

class TrailerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description='ID')
    name: str = Field(..., description="Название прицепа", max_length=200)
    description: str = Field(..., description="Описание прицепа")
    height: int = Field(..., ge=0, description="Высота прицепа (в мм) ")
    width: int = Field(..., ge=0, description="Ширина прицепа (в мм)")
    year_of_production: date = Field(..., description="Год выпуска прицепа")
    color: str = Field(..., description="Цвет прицепа", max_length=120)
    max_weight: int = Field(..., ge=0, description="Максимальная масса (в кг)")
    curb_weight: int = Field(..., ge=0, description="Масса в снаряженном состоянии (в кг)")
    deposit: int = Field(..., ge=0, description="Залоговая стоимость")
    slug: Optional[str] = Field(None, description="URL адрес", max_length=200)
    price_1: int = Field(..., description='Базовая цена')
    price_2: int = Field(..., description='Цена от 3 суток')
    price_3: int = Field(..., description='Цена от 7 суток')
    status: TrailerStatus = Field(..., description="Статус прицепа")


    @field_serializer("year_of_production")
    def serialize_year_of_production(self, year_of_production: date) -> str:
        return year_of_production.isoformat()

    @field_serializer("status")
    def serialize_status(self, status: TrailerStatus) -> str:
        return status.value

class TrailerCreateSchema(TrailerSchema):
    id: Optional[int] = None

class TrailerImageBase(BaseModel):
    trailer_id: int = Field(..., description="ID прицепа, к которому относится изображение")
    file_path: str = Field(..., description="Путь к файлу изображения")
    is_main: bool = Field(False, description="Является ли изображение главным")