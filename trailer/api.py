from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from connection_manager import manager
from models import Trailer
from mysql_db import get_db


router = APIRouter()



@router.put("/trailers/{trailer_id}")
async def update_trailer_status(trailer_id: int, status: str, session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(Trailer).where(Trailer.id == trailer_id))
    trailer = result.scalar_one_or_none()
    if not trailer:
        return {"error": "Trailer not found"}

    trailer.status = status
    await session.commit()
    await session.refresh(trailer)

    await manager.broadcast(trailer)

    return {"message": "Status updated"}