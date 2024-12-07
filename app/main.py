from fastapi import FastAPI

from app.routers import chat

app = FastAPI(
    title="Parrot OpenAI Prompt Tester API",
    description="This API allows testing of OpenAI prompts and generating responses.",
)

app.include_router(chat.router)
