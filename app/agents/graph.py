from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.state import AgentState

from app.agents.planner_agent import (
    planner_agent
)

from app.agents.retriever_agent import (
    retriever_agent
)

from app.agents.researcher_agent import (
    researcher_agent
)

from app.agents.critic_agent import (
    critic_agent
)

from app.agents.final_agent import (
    final_agent
)

# -------------------------
# Nodes
# -------------------------

def planner_node(state: AgentState):

    plan = planner_agent(
        state["question"]
    )

    return {
        "plan": plan
    }

def retrieve_node(state: AgentState):

    context = retriever_agent(
        state["question"]
    )

    return {
        "context": context
    }

def research_node(state: AgentState):

    research = researcher_agent(
        state["question"],
        state["context"]
    )

    return {
        "research": research
    }

def critic_node(state: AgentState):

    critique = critic_agent(
        state["question"],
        state["research"]
    )

    return {
        "critique": critique
    }

def final_node(state: AgentState):

    answer = final_agent(
        state["question"],
        state["context"],
        state["research"],
        state["critique"]
    )

    return {
        "answer": answer
    }

# -------------------------
# Graph
# -------------------------

workflow = StateGraph(
    AgentState
)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "retrieve",
    retrieve_node
)

workflow.add_node(
    "research",
    research_node
)

workflow.add_node(
    "critic",
    critic_node
)

workflow.add_node(
    "final",
    final_node
)

workflow.set_entry_point(
    "planner"
)

workflow.add_edge(
    "planner",
    "retrieve"
)

workflow.add_edge(
    "retrieve",
    "research"
)

workflow.add_edge(
    "research",
    "critic"
)

workflow.add_edge(
    "critic",
    "final"
)

workflow.add_edge(
    "final",
    END
)

graph = workflow.compile()