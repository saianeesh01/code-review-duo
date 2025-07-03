from crewai import Task
from ..agents.reviewer import reviewer

review_task = Task(
    agent=reviewer,
    prompt_template=(
        "You are given a pull-request diff:\n{diff}\n\n"
        "Analyse and respond with an array of ReviewComment JSON objects."
    ),
)
