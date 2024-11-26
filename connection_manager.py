import asyncio
from typing import List, Dict
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}  # Для каждого прицепа
        self.global_connections: List[WebSocket] = []  # Для глобальных обновлений

    async def connect(self, websocket: WebSocket, trailer_id: str = None):
        """Подключение клиента к определенному прицепу или ко всем прицепам"""
        await websocket.accept()

        if trailer_id:  # Если указан trailer_id, то подключаем к конкретному прицепу
            if trailer_id not in self.active_connections:
                self.active_connections[trailer_id] = []
            self.active_connections[trailer_id].append(websocket)
        else:  # Если trailer_id не указан, подключаем ко всем прицепам
            self.global_connections.append(websocket)

    def disconnect(self, websocket: WebSocket, trailer_id: str = None):
        """Отключение клиента от прицепа или всех прицепов"""
        if trailer_id:
            if trailer_id in self.active_connections:
                self.active_connections[trailer_id].remove(websocket)
        else:
            self.global_connections.remove(websocket)

    async def broadcast(self, trailer_id: str, message: dict):
        """Отправка сообщений только пользователям, отслеживающим этот прицеп"""
        if trailer_id in self.active_connections:
            for connection in self.active_connections[trailer_id]:
                await connection.send_json(message)

    async def broadcast_all(self, message: dict):
        """Отправка сообщений всем подключенным пользователям"""
        for connection in self.global_connections:
            await connection.send_json(message)

    def update_trailer_status(self, trailer_id: str, status: str):
        """Обновление статуса прицепа и трансляция всем подключенным пользователям"""
        message = {"trailer_id": trailer_id, "status": status}
        # Отправить только тем, кто отслеживает конкретный прицеп
        asyncio.create_task(self.broadcast(trailer_id, message))
        # Также отправить глобальное обновление всем пользователям
        asyncio.create_task(self.broadcast_all(message))

manager = ConnectionManager()
