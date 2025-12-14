from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel, to_snake


class Platform(str, Enum):
    walmart = "walmart"
    flipkart = "flipkart"
    eBay = "eBay"


class ScrapInput(BaseModel):
    search_query: str = Field(
        ...,
        alias="searchQuery",
        min_length=2,
        max_length=99,
        description="Search query",
    )
    platform: Platform
    page_count: int = Field(
        ..., alias="pageCount", ge=1, le=5, description="Number of pages to scrape"
    )

    model_config = ConfigDict(
        alias_generator=to_snake,
        populate_by_name=True,
    )
