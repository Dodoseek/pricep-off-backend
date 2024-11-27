from fastapi import APIRouter

from .api import router as api_router
from .websocket import router as websocket_router

router = APIRouter()

router.include_router(api_router, tags=["trailers"])
router.include_router(websocket_router, tags=["ws_trailers"])
