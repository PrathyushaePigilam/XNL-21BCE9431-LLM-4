from fastapi import APIRouter, HTTPException
from chatbot.llm_model import get_response

chatbot_router = APIRouter()

@chatbot_router.get("/chat")
async def chat_response(query: str):
    return {"response": get_response(query)}