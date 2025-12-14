from src.app.services.playwright.pw_client import PlaywrightClient


def scrape_ebay(data: dict):
    query: str = data.get("search_query", "")
    url = f"https://www.ebay.com/sch/i.html?_nkw={query}"

    with PlaywrightClient() as client:
        page = client.new_page()
        page.goto(url)
        print(page.title())
        page.close()
