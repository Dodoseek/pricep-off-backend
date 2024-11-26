from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from trailer.urls import router as trailer_urls

app = FastAPI()

origins = [
    "http://localhost:3000",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trailer_urls, prefix='/api/v1')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)