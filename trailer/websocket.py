from trailer.schema import TrailerSchema

import asyncio

from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from connection_manager import manager
from models import Trailer
from mysql_db import get_db


router = APIRouter()

@router.websocket("/ws/trailers/{trailer_id}")
async def websocket_trailer_status(websocket: WebSocket, trailer_id: str, session: AsyncSession = Depends(get_db)):
    # Подключаем клиента к отслеживанию конкретного прицепа
    await manager.connect(websocket, trailer_id)
    try:
        while True:
            await asyncio.sleep(1)
            result = await session.execute(select(Trailer).filter(Trailer.id == trailer_id))
            trailer = result.scalars().first()
            await manager.broadcast(trailer_id, trailer)
    except WebSocketDisconnect:
        manager.disconnect(websocket, trailer_id)


@router.websocket("/ws/trailers")
async def websocket_all_trailers_status(websocket: WebSocket, session: AsyncSession = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
            await session.commit()
            result = await session.execute(text("SELECT * FROM trailer"))
            trailers = result.fetchall()
            trailers_json = [TrailerSchema.from_orm(trailer).dict() for trailer in trailers]
            await manager.broadcast_all({"trailers": trailers_json})
    except WebSocketDisconnect:
        manager.disconnect(websocket)