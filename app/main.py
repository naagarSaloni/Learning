from fastapi import FastAPI

from app.graph import graph
from app.schemas import ChatRequest, ChatResponse


app = FastAPI(
    title="Mini AI Support Assistant",
    description="AI assistant built with FastAPI, LangChain and LangGraph",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mini AI Assistant is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = graph.invoke({
        "message": request.message,
        "answer": ""
    })

    return {
        "answer": result["answer"]
    }