import uuid
from fastapi import APIRouter, BackgroundTasks
from src.app.schemas.scrape import ScrapInput
from src.app.core.logging import setup_logging
import logging
from src.app.services.scraper import run_scraper

from src.app.services.jobs import jobs

setup_logging()
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/scrape")


@router.post("/")
def start_scraping(data: ScrapInput, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued"}
    background_tasks.add_task(run_scraper, data.model_dump(mode="json"), job_id)

    return {"detail": "Scraping started successfully.", "job_id": job_id}
