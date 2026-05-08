chat_memory = {}

def add_message(session_id, role, content):

    if session_id not in chat_memory:
        chat_memory[session_id] = []

    chat_memory[session_id].append({
        "role": role,
        "content": content
    })

def get_messages(session_id):
    
    return chat_memory.get(session_id, [])