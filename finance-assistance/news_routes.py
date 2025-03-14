import requests
from fastapi import APIRouter

news_router = APIRouter(prefix="/news", tags=["Financial News"])
NEWS_API_KEY = "53f4635f5d2d44f4bec30f8a41fa5083"

@news_router.get("/")
def get_financial_news():
    url = f"https://newsapi.org/v2/everything?q=finance&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    return response["articles"]
