from fastapi import FastAPI

from tools.naver_news import NaverNews
from tools.settings import settings

naver_news = NaverNews(
    client_id=settings.naver_client_id,
    client_secret=settings.naver_client_secret
)

app = FastAPI()

@app.get("/last-news/{stock}")
async def read_last_news(stock: str):
    news = await naver_news.recent_5_news(stock)
    return news