from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import random

from models.trailer.trailer import Trailer
from trailer.schema import TrailerSchema, TrailerCreateSchema
from slugify import slugify


async def get_all_trailers_from_db(session: AsyncSession):
    result = await session.execute(select(Trailer))
    trailers = result.scalars().all()
    if not trailers:
        raise HTTPException(status_code=404, detail="Данного прицепа не существует")
    return trailers


async def get_trailer_by_id_from_db(session: AsyncSession, trailer_id: int):
    result = await session.execute(select(Trailer).filter(Trailer.id == trailer_id))
    trailer = result.scalars().first()
    if not trailer:
        raise HTTPException(status_code=404, detail="Данного прицепа не существует")
    return trailer


async def is_slug_unique(session: AsyncSession, slug: str) -> bool:
    """
    Проверяет, уникален ли slug в базе данных.
    """
    result = await session.execute(select(Trailer).where(Trailer.slug == slug))
    return not result.scalars().first()

async def create_trailer_form_bd(session: AsyncSession, trailer_data: TrailerCreateSchema):
    trailer_data_dict = trailer_data.dict()
    base_slug = slugify(trailer_data_dict["name"])
    slug = base_slug
    while not await is_slug_unique(session, slug):
        slug = f"{base_slug}-{random.randint(1000, 9999)}"

    trailer_data_dict["slug"] = slug

    trailer = Trailer(**trailer_data_dict)
    session.add(trailer)
    await session.commit()
    await session.refresh(trailer)
    return trailer




async def update_trailer_from_db(session: AsyncSession, existing_trailer: Trailer, trailer_data: TrailerSchema):
    updated_data = trailer_data.dict(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_trailer, key, value)

    await session.commit()
    await session.refresh(existing_trailer)
    return existing_trailer

async def delete_trailer_form_db(session: AsyncSession, trailer: Trailer) -> None:
    await session.delete(trailer)
    await session.commit()
