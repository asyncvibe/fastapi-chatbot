"""
LLM Setup and Configuration Module
Created: June 4, 2025
Author: Hassan

This module handles the setup and configuration of Language Learning Models (LLMs)
and their associated tools. It provides the core functionality for:
1. Loading and managing API keys
2. Initializing LLM models from different providers
3. Setting up web search capabilities
4. Creating and managing AI agents with ReAct framework
"""

# Load environment variables for API keys
# Required keys:
# - GROQ_API_KEY: For accessing Groq's LLM models
# - TAVILY_API_KEY: For web search functionality
# - OPENAI_API_KEY: For accessing OpenAI models
# Initialize environment variables and API keys
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys (will be None if not found)
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Validate required API keys
if not tavily_api_key:
    print("Warning: TAVILY_API_KEY not found. Web search will be disabled.")
if not (groq_api_key or openai_api_key):
    raise ValueError("Either GROQ_API_KEY or OPENAI_API_KEY must be provided.")

# Import required LLM and tool components
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent



def llm_agent_func(system_prompt, query, provider, model_name, allow_search):
    """
    Creates and invokes an AI agent with optional web search capabilities.
    
    This function is the core of the AI chat system. It:
    1. Validates API keys and configurations
    2. Sets up the appropriate LLM based on the provider
    3. Configures web search tools if enabled
    4. Creates a ReAct agent with the specified system prompt
    5. Processes the user query with error handling
    6. Returns formatted response or error message
    
    Args:
        system_prompt (str): Initial prompt defining the AI's behavior and context
        query (str): The user's input or question
        provider (str): LLM provider ("Openai" or "Groq")
        model_name (str): Name of the specific model to use
        allow_search (bool): Whether to enable web search capabilities
    
    Returns:
        str: The AI's response to the query
    
    Example:
        response = llm_agent_func(
            "You are a helpful assistant",
            "What is FastAPI?",
            "Groq",
            "llama-3.3-70b-versatile",
            True
        )
    """
    try:
        # Validate API keys based on provider
        if provider == "Openai" and not openai_api_key:
            return "Error: OpenAI API key not configured"
        elif provider == "Groq" and not groq_api_key:
            return "Error: Groq API key not configured"
            
        # Configure search tool if enabled and API key is available
        if allow_search:
            if not tavily_api_key:
                return "Error: Tavily API key required for web search"
            search_tool = [TavilySearchResults(max_results=2)]
        else:
            search_tool = []
        
        # Initialize the appropriate LLM based on provider
        if provider == "Openai":
            llm = ChatOpenAI(model=model_name)  # OpenAI parameter is 'model'
        elif provider == "Groq":
            llm = ChatGroq(model=model_name)    # Groq parameter is 'model'
        else:
            return f"Error: Unsupported provider {provider}"
    
    # Create ReAct agent with tools and system prompt
    agent = create_react_agent(
        model=llm,
        tools=search_tool,
        prompt=system_prompt
    )
    
    # Process query and get response
    response = agent.invoke(
        {"messages": [HumanMessage(content=query)]}
    )
    
    # Extract and return the AI's last message with error handling
        messages = response.get("messages", [])
        ai_message = [
            message.content 
            for message in messages 
            if isinstance(message, AIMessage)
        ]
        
        if ai_message:
            response_text = ai_message[-1]
            print(f"AI Response: {response_text}")  # Log successful response
            return response_text
        else:
            error_msg = "No valid AI response generated"
            print(f"Error: {error_msg}")  # Log error
            return f"Error: {error_msg}"
            
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        print(f"Error: {error_msg}")  # Log error for debugging
        return f"Error: {error_msg}"
