from fastapi import APIRouter, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

YODLEE_CLIENT_ID = os.getenv("YODLEE_CLIENT_ID")
YODLEE_SECRET = os.getenv("YODLEE_SECRET")
YODLEE_BASE_URL = "https://sandbox.api.yodlee.com/ysl"

banking_router = APIRouter(prefix="/banking", tags=["Banking API"])

def get_yodlee_access_token():
    url = f"{YODLEE_BASE_URL}/auth/token"
    headers = {
        "Api-Version": "1.1",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "clientId": YODLEE_CLIENT_ID,
        "secret": YODLEE_SECRET
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get("token", "")
    else:
        return None

@banking_router.get("/transactions")
def get_bank_transactions(account_id: str = None, from_date: str = None, to_date: str = None, limit: int = 10):
    """
    Fetch bank transactions with optional filters:
    - account_id: Filter by a specific bank account
    - from_date: Start date (YYYY-MM-DD)
    - to_date: End date (YYYY-MM-DD)
    - limit: Number of transactions to retrieve (default: 10)
    """
    token = get_yodlee_access_token()
    if not token:
        raise HTTPException(status_code=401, detail="Failed to retrieve access token")

    url = f"{YODLEE_BASE_URL}/accounts/transactions"
    headers = {"Authorization": f"Bearer {token}"}

    params = {"limit": limit}
    if account_id:
        params["accountId"] = account_id
    if from_date:
        params["fromDate"] = from_date
    if to_date:
        params["toDate"] = to_date

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch transactions")
