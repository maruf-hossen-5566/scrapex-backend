import json
from src.app.services.playwright.pw_client import PlaywrightClient

from rich import print


def scrape_walmart(data: dict):
    query: str = data.get("search_query", "")
    url = f"https://www.walmart.com/search?q={query}"
    products = None

    with PlaywrightClient() as client:
        page = client.new_page()
        page.set_default_timeout(120000)
        page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        page.goto(url)
        script = page.locator("script#__NEXT_DATA__").text_content()
        if script:
            products = json.loads(script)["props"]["pageProps"]["initialData"][
                "searchResult"
            ]["itemStacks"][0]["items"]

        page.close()

    return products
