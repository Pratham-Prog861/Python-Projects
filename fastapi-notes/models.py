from bson import ObjectId
from datetime import datetime

def note_helper(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "content": note.get("content"),
        "created_at": note["created_at"],
        "updated_at": note.get("updated_at"),
    }

def new_note(title: str, content: str | None):
    return {
        "title": title,
        "content": content,
        "created_at": datetime.utcnow(),
        "updated_at": None,
    }
