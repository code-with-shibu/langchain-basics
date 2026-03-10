from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from agent.utils.system_prompt import CHAT_AGENT_SYSTEM_PROMPT
from langchain.agents import create_agent
from dotenv import load_dotenv
from agent.utils.tools import add_numbers, multiply_numbers, result_formatter
import os

load_dotenv()


class LLMClient:
    def __init__(self):

        model = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite-preview",
            api_key = os.getenv("GEMINI_API_KEY"),
            temperature=0.5,
            max_tokens=None,
            timeout=10,
            max_retries=3
        )

        self.agent = create_agent(
            model=model,
            system_prompt=CHAT_AGENT_SYSTEM_PROMPT,
            checkpointer=InMemorySaver(),
            tools=[multiply_numbers, add_numbers, result_formatter]
        )
        

llm_client = LLMClient()



