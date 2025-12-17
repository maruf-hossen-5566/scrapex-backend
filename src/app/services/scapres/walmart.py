import json
from src.app.core.config import settings
from src.app.services.exceptions import ScraperError
from rich import print
import logging
from src.app.core.logging import setup_logging
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup


setup_logging()
logger = logging.getLogger(__name__)


def extract_script_tag(html):
    soup = BeautifulSoup(html, "html.parser")
    script_tag = soup.find("script", attrs={"id": "__NEXT_DATA__"}).get_text().strip()  # type: ignore

    if not script_tag:
        raise ScraperError("Walmart data script not found!")

    products = json.loads(script_tag)["props"]["pageProps"]["initialData"][
        "searchResult"
    ]["itemStacks"][0]["items"]
    return products


def scrape_walmart(d: dict):
    query: str = quote(d.get("search_query", ""))

    api_key = settings.BRIGHT_DATA_API
    zone = settings.BRIGHT_DATA_ZONE

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "zone": zone,
        "url": f"https://www.walmart.com/search?q={query}",
        "format": "raw",
    }
    response = requests.post(
        "https://api.brightdata.com/request", json=data, headers=headers
    )

    if not response.status_code == 200:
        raise ScraperError("Failed to get data for Bright-Data")

    with open("walmart.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    return extract_script_tag(response.text)
