from app.memory.session_memory import (
    save_message,
    get_messages
)

from app.memory.semantic_memory import (
    store_memory,
    retrieve_memory
)

def add_to_memory(
    session_id,
    role,
    content
):

    save_message(
        session_id,
        role,
        content
    )

    store_memory(
        session_id,
        f"{role}: {content}"
    )

def get_full_memory(
    session_id,
    question
):

    chat_history = get_messages(
        session_id
    )

    semantic_memories = retrieve_memory(
        session_id,
        question
    )

    return {
        "chat_history": chat_history,
        "semantic_memories": semantic_memories
    }