import uuid
from fastapi import APIRouter, BackgroundTasks
from src.app.schemas.scrape import ScrapInput
from src.app.core.logging import setup_logging
import logging
from src.app.services.scraper import run_scraper
from rich import print

from src.app.services.jobs import jobs

setup_logging()
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/scrape")


@router.post("/")
def start_scraping(data: ScrapInput, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued"}
    background_tasks.add_task(run_scraper, data.model_dump(mode="json"), job_id)
    # print(data.model_dump(mode="json"))

    return {"detail": "Scraping started successfully.", "id": job_id}


@router.get("/{job_id}")
def get_scraped_data(job_id: str):
    logger.info(f"JOB_ID: {job_id}")
    job = jobs[job_id]
    return {"detail": "Scrapping finished successfully.", "data": job}
