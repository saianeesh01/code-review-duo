from crewai import Agent
from litellm import completion
from ..models.schemas import DiffPatch
from ..config import CHAT_MODEL, OLLAMA_BASE

def ollama_chat(messages, **kw):
    return completion(model=f"ollama/{CHAT_MODEL}",
                      base_url=OLLAMA_BASE, messages=messages, **kw)

fixer = Agent(
    name="Fix-Bot",
    system_prompt=(
        "Given review comments, output a unified git diff that "
        "addresses them. Validate against DiffPatch schema."
    ),
    llm=ollama_chat,
    output_schema=DiffPatch,
)
