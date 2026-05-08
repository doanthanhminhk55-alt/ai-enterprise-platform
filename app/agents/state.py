from typing import TypedDict

class AgentState(TypedDict):

    session_id: str

    question: str

    memory: str

    plan: str

    context: str

    research: str

    critique: str

    answer: str