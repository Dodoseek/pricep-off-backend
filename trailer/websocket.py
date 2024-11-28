from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from connection_manager import manager


router = APIRouter()


@router.websocket("/ws/trailers")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket-эндпоинт для установления соединения с клиентом"""
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)