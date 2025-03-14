import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Yodlee API Credentials
YODLEE_CLIENT_ID = os.getenv("YODLEE_CLIENT_ID")
YODLEE_SECRET = os.getenv("YODLEE_SECRET")

# Alpha Vantage API Key (for stock market data)
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# MongoDB Connection String
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/financial_assistant")

# FastAPI Settings (optional)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
