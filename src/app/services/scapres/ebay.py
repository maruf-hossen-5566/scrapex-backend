from src.app.services.playwright.pw_client import PlaywrightClient
import json


def scrape_ebay(data: dict):
    query: str = data.get("search_query", "")
    url = f"https://www.ebay.com/sch/i.html?_nkw={query}"

    with PlaywrightClient() as client:
        page = client.new_page()
        page.goto(url)
        ld_json = page.locator("script[typs='application/ld+json']").all_inner_texts()
        print("-" * 100)
        print("eBay data: ", ld_json)
        print("-" * 100)
        page.close()
