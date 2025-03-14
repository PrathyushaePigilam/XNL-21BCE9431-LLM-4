from fastapi import FastAPI
from backend.routes import chatbot_routes, stock_routes, crypto_routes, banking_routes, news_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chatbot_routes.chatbot_router)
app.include_router(stock_routes.stock_router)
app.include_router(crypto_routes.crypto_router)
app.include_router(banking_routes.banking_router)
app.include_router(news_routes.news_router)

@app.get("/")
def root():
    return {"message": "Financial Assistant API is running!"}
