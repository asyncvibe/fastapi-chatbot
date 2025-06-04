# step 1: setup UI with streamlit
import streamlit as st
import requests
st.set_page_config(page_title="FastAPI AI Agent", page_icon="🤖", layout="centered")
st.title("FastAPI AI Agent")
st.write("create and interact with ai agents using fastapi")
system_prompt = st.text_area("define your AI agent",height=70, placeholder="type your system prompts here")
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]
provider = st.radio("Select Provider:",("Groq","Openai"))
if provider == "Groq":
    model_name = st.selectbox("Select Groq Model Name:", MODEL_NAMES_GROQ)
elif provider == "Openai":
    model_name = st.selectbox("Select Openai Model Name:", MODEL_NAMES_OPENAI)
allow_web_search = st.checkbox("Allow Search?", value=True)
user_query = st.text_area("type your query",height=150, placeholder="Ask anything")
API_URL="http://127.0.0.1:8000/api/chat"
if st.button("Ask anything"):
    if user_query.strip():
        payload={
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "query": user_query,
            "allow_search": allow_web_search
        }
        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            # response = response_data["response"]
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Response:** {response_data}")
    # get response from backend and display it
    