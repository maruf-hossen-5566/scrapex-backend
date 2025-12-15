from playwright.sync_api import sync_playwright, Browser, Playwright, BrowserContext
from src.app.core.config import settings


class PlaywrightClient:
    def __init__(self, headless: bool = False) -> None:
        self.headless = headless
        self.playwright: Playwright | None = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.proxy = {
            "server": settings.PROXY_SERVER,
            "username": settings.PROXY_USERNAME,
            "password": settings.PROXY_PASSWORD,
        }

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=["--disable-blink-features=AutomationControlled"],
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def new_page(self):
        self.context = self.browser.new_context(
            proxy=self.proxy,
            locale="en-US",
            timezone_id="America/New_York",
        )
        page = self.context.new_page()
        page.set_default_timeout(60000)
        return page
