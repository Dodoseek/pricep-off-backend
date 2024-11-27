from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class TrailerImage(Base):
    __tablename__ = "trailer_image"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    trailer_id = Column(BigInteger, ForeignKey("trailer.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String(300), nullable=False, comment="Путь к изображению")
    description = Column(String(200), nullable=True, comment="Описание изображения")

    # Связь с моделью Trailer
    trailer = relationship("Trailer", back_populates="images")

    images = relationship(
        "TrailerImage",
        back_populates="trailer",
        cascade="all, delete-orphan",
    )