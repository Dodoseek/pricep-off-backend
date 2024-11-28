from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from connection_manager import manager
from models import Trailer
from mysql_db import get_db
from trailer.schema import TrailerSchema
from trailer.services import get_trailer_by_id_from_db, delete_trailer_form_db, create_trailer_form_bd, \
    update_trailer_from_db, get_all_trailers_from_db

router = APIRouter()


@router.get('/trailers', response_model=List[TrailerSchema])
async def get_all_trailers(session: AsyncSession = Depends(get_db)):
    return get_all_trailers_from_db(session)


@router.get('/trailers/{trailer_id}', response_model=TrailerSchema)
async def get_trailer_by_id(trailer_id: int, session: AsyncSession = Depends(get_db)):
    return await get_trailer_by_id_from_db(session, trailer_id)


@router.post("/trailers", response_model=TrailerSchema)
async def create_trailer(trailer_data: TrailerSchema, session: AsyncSession = Depends(get_db)):
    trailer = await create_trailer_form_bd(session, trailer_data)
    await manager.broadcast(trailer)
    return trailer


@router.put("/trailers/{trailer_id}", response_model=TrailerSchema)
async def update_trailer(trailer_id: int, trailer_data: TrailerSchema, session: AsyncSession = Depends(get_db)):
    existing_trailer = await get_trailer_by_id_from_db(session, trailer_id)
    new_trailer = await update_trailer_from_db(session, existing_trailer, trailer_data)
    await manager.broadcast(new_trailer)
    return new_trailer


@router.delete("/trailers/{trailer_id}", response_model=TrailerSchema)
async def delete_trailer(trailer_id: int, session: AsyncSession = Depends(get_db)):
    trailer = await get_trailer_by_id_from_db(session, trailer_id)
    await delete_trailer_form_db(session, trailer)
    await manager.broadcast(trailer)
    return trailer
