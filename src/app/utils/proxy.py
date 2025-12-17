from src.app.core.config import settings


def get_proxy():
    p = {
        "server": settings.PROXY_SERVER,
        "username": settings.PROXY_USERNAME,
        "password": settings.PROXY_PASSWORD,
    }
    return p
