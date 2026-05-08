from typing import TypedDict

class AgentState(TypedDict):

    question: str

    plan: str

    context: str

    research: str

    critique: str

    answer: str