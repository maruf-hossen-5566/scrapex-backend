from fake_useragent import UserAgent
import random


def generate_random_headers():
    ua = UserAgent()
    # "User-Agent": ua.random,
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": random.choice(
            [
                "https://www.google.com/",
                "https://www.bing.com/",
                "https://www.yahoo.com/",
                "https://duckduckgo.com/",
            ]
        ),
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
    }
    return headers
