from pydantic import BaseModel

class ChatRequest(BaseModel):
    persona: str
    message: str
