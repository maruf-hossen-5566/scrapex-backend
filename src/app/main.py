from fastapi import FastAPI
from src.app.api import scrape_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(scrape_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
