# FastAPI AI Chatbot

A modern AI chatbot backend built with FastAPI that supports multiple LLM providers and includes web search capabilities.

## Features

- 🚀 Fast and async API powered by FastAPI
- 🤖 Support for multiple LLM providers:
  - OpenAI
  - Groq
- 🔍 Web search integration using Tavily
- ⚡ Real-time chat responses
- 🛡️ Input validation using Pydantic
- 📝 System prompt customization
- 🔄 Conversation history support

## Prerequisites

- Python 3.12+
- API keys for:
  - OpenAI or Groq (LLM providers)
  - Tavily (for web search capability)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables by creating a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

## Usage

1. Start the FastAPI server:
```bash
python backend.py
```

2. The server will start at `http://127.0.0.1:8000`

3. Access the API documentation at `http://127.0.0.1:8000/docs`

### API Endpoints

#### POST /api/chat
Send a chat message to the AI agent.

Request body:
```json
{
  "model_name": "string",
  "model_provider": "string",
  "system_prompt": "string",
  "messages": ["string"],
  "allow_search": boolean
}
```

Supported models:
- llama3-70b-8192
- mixtral-8x7b-32768
- llama-3.3-70b-versatile
- gpt-4o-mini

## Project Structure

- `backend.py` - FastAPI application and API endpoints
- `frontend.py` - Frontend interface (to be implemented)
- `llm_setup.py` - LLM configuration and chat agent setup

## Error Handling

The API includes comprehensive error handling for:
- Invalid model names
- Missing API keys
- LLM provider errors
- Invalid requests

## TODO List for Future Improvements

1. Authentication & Security
   - [ ] Add API key authentication
   - [ ] Implement rate limiting
   - [ ] Add request validation middleware

2. Enhanced Features
   - [ ] Add streaming response support
   - [ ] Implement conversation memory
   - [ ] Add support for more LLM providers
   - [ ] Add chat history persistence
   - [ ] Implement token counting and management

3. Frontend Development
   - [ ] Create a web-based chat interface
   - [ ] Add real-time response streaming
   - [ ] Implement conversation threading
   - [ ] Add markdown rendering support

4. Performance Improvements
   - [ ] Add response caching
   - [ ] Implement request queuing
   - [ ] Add load balancing support
   - [ ] Optimize prompt handling

5. Developer Experience
   - [ ] Add comprehensive tests
   - [ ] Improve logging and monitoring
   - [ ] Add Docker support
   - [ ] Create CI/CD pipeline

6. Documentation
   - [ ] Add API documentation
   - [ ] Create setup guide for different environments
   - [ ] Add examples and use cases
   - [ ] Document all configuration options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Support

For support, please open an issue in the repository.