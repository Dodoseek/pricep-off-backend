from pydantic import BaseModel, Field, ConfigDict


class TrailerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., description="Название прицепа")
    description: str = Field(..., description="Описание прицепа")
    height: int = Field(..., ge=0, description="Высота прицепа (в мм) ")
    width: int = Field(..., ge=0, description="Ширина прицепа (в мм)")
    year_of_production: str = Field(..., description="Год выпуска прицепа")
    color: str = Field(..., description="Цвет прицепа")
    max_weight: int = Field(..., ge=0, description="Максимальная масса (в кг)")
    curb_weight: int = Field(..., ge=0, description="Масса в снаряженном состоянии (в кг)")
    deposit: int = Field(..., ge=0, description="Залоговая стоимость")
    slug: str = Field(..., description="URL адрес")
    price_1: int = Field(..., description='Базовая цена')
    price_2: int = Field(..., description='Цена от 3 суток')
    price_3: int = Field(..., description='Цена от 7 суток')


