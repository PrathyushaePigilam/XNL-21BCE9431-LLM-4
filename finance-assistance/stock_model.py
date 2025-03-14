from pydantic import BaseModel
from typing import Optional

class Stock(BaseModel):
    symbol: str  # Stock ticker symbol (e.g., AAPL, TSLA)
    name: str  # Company name
    price: float  # Current stock price
    change: float  # Price change
    percent_change: float  # Percentage change in price
    volume: Optional[int] = None  # Trading volume (optional)
    market_cap: Optional[float] = None  # Market capitalization (optional)
