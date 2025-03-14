from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    role: str  # "system", "user", or "assistant"
    content: str  # The actual message text

class ChatRequest(BaseModel):
    messages: List[ChatMessage]  # List of messages exchanged in a conversation

class ChatResponse(BaseModel):
    response: str  # The chatbot's reply
