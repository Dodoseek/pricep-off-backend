import asyncio
from typing import List, Dict
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Подключение клиента к определенному прицепу или ко всем прицепам"""
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Отключение клиента от прицепа или всех прицепов"""
        self.connections.remove(websocket)

    async def broadcast(self, message: dict):
        """Отправка сообщений всем подключенным пользователям"""
        for connection in self.connections:
            await connection.send_json(message)


manager = ConnectionManager()
