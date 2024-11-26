from sqlalchemy import (
    Column, String, Integer, BigInteger, Text, Date
)

from models.base import Base


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
    deposit = Column(Integer, nullable=False, comment="Залог")
    slug = Column(String(200), unique=True, nullable=False, comment="URL")
    price_1 = Column(Integer, nullable=False, comment="Базовая цена")
    price_2 = Column(Integer, nullable=False, comment="Цена от 3 суток")
    price_3 = Column(Integer, nullable=False, comment="Цена от 7 суток")