from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.handlers.kubernetes_handler import get_cluster_info
from app.chatbot.rasa_bot import process_message

app = FastAPI(title="K8s Monitoring Chatbot")

# Define request body model for /chat
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Kubernetes Monitoring Chatbot!"}

@app.get("/k8s/info")
def cluster_info():
    try:
        info = get_cluster_info()
        return {"cluster_info": info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        response = await process_message(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
