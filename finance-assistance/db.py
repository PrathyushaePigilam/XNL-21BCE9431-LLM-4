from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.financial_db  # Database Name

# Collections
stock_collection = db.stocks
crypto_collection = db.cryptos
banking_collection = db.bank_transactions
chatbot_logs = db.chatbot_logs
