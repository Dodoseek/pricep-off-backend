from sqlalchemy import Column, String, BigInteger, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import Base


class TrailerImage(Base):
    __tablename__ = "trailer_image"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    trailer_id = Column(BigInteger, ForeignKey("trailer.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String(300), nullable=False, comment="Путь к изображению")
    is_main = Column(Boolean, nullable=False, default=False, comment="Является ли изображение главным")

    trailer = relationship("Trailer", back_populates="images")
