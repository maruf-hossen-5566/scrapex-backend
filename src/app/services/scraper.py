import logging
from src.app.core.logging import setup_logging
from src.app.services.jobs import jobs
from src.app.services.scapres.ebay import scrape_ebay
from src.app.services.scapres.flipkar import scrape_flipkart
from src.app.services.scapres.walmart import scrape_walmart

setup_logging()
logger = logging.getLogger(__name__)


def run_scraper(data: dict, job_id: str):
    jobs[job_id] = {"status": "running"}
    try:
        result = scrape(data)
        jobs[job_id] = {"status": "finished", "data": result}
    except Exception as e:
        logger.exception("Failed to scrape")
        jobs[job_id] = {"status": "failed", "error": str(e)}


def scrape(data: dict):
    platform: str = data.get("platform", "")

    if platform and platform.strip().lower() == "walmart":
        return scrape_walmart(data)

    if platform and platform.strip().lower() == "flipkart":
        return scrape_flipkart(data)

    return scrape_ebay(data)
