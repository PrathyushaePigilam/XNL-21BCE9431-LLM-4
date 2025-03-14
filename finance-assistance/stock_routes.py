import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

stock_router = APIRouter(prefix="/stocks", tags=["Stock Data"])
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")  

class StockData(BaseModel):
    symbol: str
    interval: str
    open: float
    high: float
    low: float
    close: float
    volume: int

@stock_router.get("/{symbol}", response_model=list[StockData])
def get_stock_data(symbol: str, interval: str = "5min"):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}"
    response = requests.get(url).json()

    time_series_key = f"Time Series ({interval})"
    
    if time_series_key in response:
        data = response[time_series_key]
        stock_data_list = []

        for timestamp, values in data.items():
            stock_data_list.append(
                StockData(
                    symbol=symbol,
                    interval=interval,
                    open=float(values["1. open"]),
                    high=float(values["2. high"]),
                    low=float(values["3. low"]),
                    close=float(values["4. close"]),
                    volume=int(values["5. volume"]),
                )
            )
        
        return stock_data_list 
    
    raise HTTPException(status_code=400, detail="Invalid stock symbol or API error")
