from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.trailer.trailer import Trailer
from trailer.schema import TrailerSchema


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


async def create_trailer_form_bd(session: AsyncSession, trailer_data: TrailerSchema):
    trailer_data_dict = trailer_data.dict()
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
