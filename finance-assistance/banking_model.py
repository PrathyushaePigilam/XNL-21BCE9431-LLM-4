from pydantic import BaseModel
from typing import List

class Transaction(BaseModel):
    id: str
    amount: float
    date: str
    description: str
    category: str

class TransactionsResponse(BaseModel):
    transactions: List[Transaction]
