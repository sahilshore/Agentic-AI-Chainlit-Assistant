import os
import nest_asyncio
import chainlit as cl
from dotenv import load_dotenv

# --------------------------------------------------
# LlamaIndex imports
# --------------------------------------------------
from llama_index.core import Settings
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.groq import Groq

# --------------------------------------------------
# Fix async loop issues (important for Chainlit)
# --------------------------------------------------
nest_asyncio.apply()

# --------------------------------------------------
# Load environment variables from .env
# --------------------------------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Please set it in .env file")

# --------------------------------------------------
# Initialize LLM (Groq)
# --------------------------------------------------
llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)

Settings.llm = llm

# --------------------------------------------------
# Define tool functions
# --------------------------------------------------
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result"""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and return the result"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two integers and return the result"""
    return a - b


def divide(a: int, b: int) -> float:
    """Divide two integers and return the result"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# --------------------------------------------------
# Convert functions to LlamaIndex tools
# --------------------------------------------------
multiply_tool = FunctionTool.from_defaults(fn=multiply)
add_tool = FunctionTool.from_defaults(fn=add)
subtract_tool = FunctionTool.from_defaults(fn=subtract)
divide_tool = FunctionTool.from_defaults(fn=divide)

# --------------------------------------------------
# Create ReAct Agent
# --------------------------------------------------
agent = ReActAgent(
    tools=[multiply_tool, add_tool, subtract_tool, divide_tool],
    llm=llm,
    verbose=True
)


# --------------------------------------------------
# Chainlit lifecycle
# --------------------------------------------------
@cl.on_chat_start
async def on_chat_start():
    """Runs when chat UI loads"""
    await cl.Message(
        content="👋 Hello! I am an **Agentic AI Assistant**.\n\nI can solve math problems using tools.\n\nTry something like:\n`(65 * 7) / 8`"
    ).send()

    cl.user_session.set("agent", agent)


@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")

    response = await agent.run(message.content)

    await cl.Message(content=str(response)).send()
