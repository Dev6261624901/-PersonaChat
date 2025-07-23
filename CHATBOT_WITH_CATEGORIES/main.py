from fastapi import FastAPI, HTTPException
from models import ChatRequest
from gemini import chat_with_gemini
from Categories import PERSONAS

app = FastAPI()

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    if req.persona not in PERSONAS:
        raise HTTPException(status_code=400, detail="Invalid categories selected.")

    persona_prompt = PERSONAS[req.persona]
    full_prompt = f"{persona_prompt}\n\nUser: {req.message}\nBot:"
    
    try:
        reply = chat_with_gemini(full_prompt)
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
