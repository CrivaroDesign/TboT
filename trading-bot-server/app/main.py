from fastapi import FastAPI
from app.routes import bot

app = FastAPI(title="Trading Bot API")

# Register API routes
app.include_router(bot.router)
