from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model untuk pesan
class Message(BaseModel):
    sender: str
    receiver: str
    text: str

# Database sementara
messages = []

@app.post("/send/")
def send_message(message: Message):
    messages.append(message)
    return {"message": "Pesan berhasil dikirim!"}

@app.get("/messages/", response_model=List[Message])
def get_messages():
    return messages

@app.delete("/clear/")
def clear_messages():
    messages.clear()
    return {"message": "Semua pesan telah dihapus!"}
