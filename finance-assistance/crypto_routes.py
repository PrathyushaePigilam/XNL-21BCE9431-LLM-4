import requests
from fastapi import APIRouter

crypto_router = APIRouter(prefix="/crypto", tags=["Crypto Data"])

@crypto_router.get("/{crypto}")
def get_crypto_data(crypto: str = "bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url).json()
    return response
