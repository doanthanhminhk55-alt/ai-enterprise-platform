from app.memory.redis_client import redis_client
import json

def save_message(
    session_id,
    role,
    content
):
    key = f"chat:{session_id}"

    messages = get_messages(session_id)

    messages.append({
        "role": role,
        "content": content
    })

    redis_client.set(
        key,
        json.dumps(messages)
    )

def get_messages(session_id):

    key = f"chat:{session_id}"

    data = redis_client.get(key)

    if not data:
        return []
    
    return json.loads(data)