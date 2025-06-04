# step 1: Setup Pydantic Model (schema validation)
from pydantic import BaseModel
from llm_setup import llm_agent_func
# from typing import List
import uvicorn

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    query: str
    allow_search: bool
# step 2: Setup AI Agent from Frontend requests using fastapi
from fastapi import FastAPI
app = FastAPI(title="AI Agent")

ALLOWED_MODELS_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

@app.post("/api/chat")
async def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODELS_NAMES:
        return {"error": "Model name not allowed"}
    # create LLM and get response from it
    response = llm_agent_func(request.system_prompt, request.query, request.model_provider, request.model_name, request.allow_search)
    return response
    
  
# step 3: Run app and explore swagger UI Docs
if __name__ == "__main__":
    # making localhost for our app, so we can talk with above code.
    uvicorn.run(app, host="127.0.0.1", port=8000)