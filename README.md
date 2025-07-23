PersonaChat is a FastAPI-based chatbot powered by Gemini-Pro that allows users to interact with an AI in different persona modes like teacher, scientist, friend, and more. Each persona offers unique, context-aware, personality-driven responses tailored to the selected behavior.

🚀 Features
🔮 Powered by Gemini-Pro (Google Generative AI)

👤 Persona-based chat experience: Select from teacher, scientist, friend, and more

⚡ Built using FastAPI — blazing fast and easy to scale

📦 Modular code: neatly structured by responsibilities

🧪 Swagger/OpenAPI docs enabled

🔒 Secure and clean API request handling
CHATBOT_WITH_CATEGORIES/
├── Categories.py         # Contains persona definition and behavior selection
├── gemini.py             # Handles Gemini-Pro API calls
├── main.py               # FastAPI app and routing
├── models.py             # Pydantic request/response models
├── requirements.txt      # Python dependencies
📦 Installation & Setup
1. Clone the Repo
git clone https://github.com/Dev6261624901/-PersonaChat.git
cd -PersonaChat/CHATBOT_WITH_CATEGORIES
2. Create & Activate a Virtual Environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Set Your Gemini-Pro API Key
Create a .env file or modify gemini.py to include your Google Generative AI API key.
env
GEMINI_API_KEY=your_api_key_here
5. Run the App
uvicorn main:app --reload
Then visit http://localhost:8000/docs to interact via Swagger UI.
🔧 Example Usage
Hit the /chat endpoint with JSON like:
{
  "persona": "teacher",
  "message": "What is Newton's second law?"
}
Response:
{
  "response": "Newton's second law states that Force = Mass × Acceleration..."
}
