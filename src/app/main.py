from fastapi import FastAPI
from src.app.api import scrape_router

app = FastAPI()
app.include_router(scrape_router.router)
