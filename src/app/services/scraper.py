import random
import time
import logging
from src.app.core.logging import setup_logging
from src.app.services.exceptions import ScraperError
from src.app.services.jobs import jobs
from src.app.services.scapres.walmart import scrape_walmart
from src.app.utils.scraper_helper import clean_walmart_results

setup_logging()
logger = logging.getLogger(__name__)


def run_scraper(data: dict, job_id: str):
    jobs[job_id] = {"status": "running"}
    try:
        platform, results = scrape(data)
        jobs[job_id] = {
            "status": "finished",
            "data": {"platform": platform, "items": results},
        }
    except ScraperError as e:
        logger.exception(str(e))
        jobs[job_id] = {"status": "failed", "error": str(e)}
    except Exception as e:
        logger.exception("Unexpected error")
        jobs[job_id] = {"status": "failed", "error": "Internal Server Error"}


def scrape(data: dict):
    results = scrape_walmart(data)
    return "walmart", clean_walmart_results(results)
