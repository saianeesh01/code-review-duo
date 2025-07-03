from crewai import Agent
from litellm import completion
from ..models.schemas import ReviewComment
from ..config import CHAT_MODEL, OLLAMA_BASE

def ollama_chat(messages, **kw):
    return completion(model=f"ollama/{CHAT_MODEL}",
                      base_url=OLLAMA_BASE, messages=messages, **kw)

reviewer = Agent(
    name="Review-Bot",
    system_prompt=(
        "You are a senior code reviewer. "
        "Return ONLY JSON that validates against ReviewComment[]."
    ),
    llm=ollama_chat,
    output_schema=ReviewComment,
)
