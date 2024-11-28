import enum

from sqlalchemy import (
    Column, String, Integer, BigInteger, Text, Date, Enum
)
from sqlalchemy.orm import relationship, validates

from models.base import Base


class TrailerStatus(enum.Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    UNAVAILABLE = "unavailable"

class Trailer(Base):
    __tablename__ = "trailer"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False, comment="Название прицепа")
    description = Column(Text, nullable=False, comment="Описание")
    height = Column(Integer, nullable=False, comment="Высота")
    width = Column(Integer, nullable=False, comment="Ширина")
    year_of_production = Column(Date, nullable=False, comment="Год производства")
    color = Column(String(120), nullable=False, comment="Цвет")
    max_weight = Column(Integer, nullable=False, comment="Максимальная масса")
    curb_weight = Column(Integer, nullable=False, comment="Масса в снаряженном состоянии")
    deposit = Column(Integer, nullable=False, comment="Залог", default=3000)
    slug = Column(String(200), unique=True, nullable=False, comment="URL")
    price_1 = Column(Integer, nullable=False, default=800, comment="Базовая цена")
    price_2 = Column(Integer, nullable=False, default=700, comment="Цена от 3 суток")
    price_3 = Column(Integer, nullable=False, default=600, comment="Цена от 7 суток")
    status = Column(Enum(TrailerStatus), nullable=False, default=TrailerStatus.AVAILABLE)

    images = relationship(
        "TrailerImage",
        back_populates="trailer",
        cascade="all, delete-orphan",
    )

    @validates("height", "width", "max_weight", "curb_weight")
    def validate_positive_values(self, key, value):
        if value <= 0:
            raise ValueError(f"{key.capitalize()} должно быть положительным числом.")
        return value