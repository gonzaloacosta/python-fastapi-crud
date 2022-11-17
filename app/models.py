import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Article(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    article_id: str = Field(...)
    title: str = Field(...)
    body: str = Field(...)
    detected_language: str = Field(...)
    license: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "article_id": "202208080132AMSPIDERFIN_NEWS_147629_4651215",
                "title": "Bearish block trade of TIANQI LITHIUM(09696) 73.8K shares at $81.9, $6.044M turnover [AAStocks Financial News (China)]",
                "body": "last price is up 1.739%. Today's highest price is $82.85 and lowest price is $80.25. \nTotal volume is 3.727M shares and total turnover is HK$305.355M.",
                "date": "2022-08-08",
                "detected_language": "en",
                "license": "none"
            }
        }


class ArticleUpdate(BaseModel):
    article_id: Optional[str]
    title: Optional[str]
    body: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "article_id": "202208080132AMSPIDERFIN_NEWS_147629_4651216",
                "title": "Bearish block trade of TIANQI LITHIUM(09696) 73.9K shares at $82.9, $6.044M turnover [AAStocks Financial News (China)]",
                "body": "last price is up 1.729%. Today's highest price is $82.89 and lowest price is $80.23. \nTotal volume is 3.727M shares and total turnover is HK$305.355M.",
            }
        }
