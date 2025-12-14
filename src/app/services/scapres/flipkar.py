from src.app.services.playwright.pw_client import PlaywrightClient


def scrape_flipkart(data: dict):
    query: str = data.get("search_query", "")
    url = f"https://www.flipkart.com/search?q={query}"

    with PlaywrightClient() as client:
        page = client.new_page()
        page.goto(url)
        print(page.title())
        page.close()
