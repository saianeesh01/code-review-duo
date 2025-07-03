from crewai import Task
from ..agents.fixer import fixer
from .review_task import review_task

fix_task = Task(
    agent=fixer,
    input=review_task,                      # chain-input
    prompt_template=(
        "Using these review comments:\n{comments}\n"
        "Fetch any missing context with get_context(file,line) and "
        "output a DiffPatch JSON."
    ),
)
