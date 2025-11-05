from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from datetime import datetime
import schemas
from database import notes_collection
from models import note_helper, new_note

app = FastAPI(title="Notes API with MongoDB Atlas")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/notes/", response_model=schemas.NoteOut)
def create_note(note_in: schemas.NoteCreate):
    note_data = new_note(note_in.title, note_in.content)
    result = notes_collection.insert_one(note_data)
    note_data["_id"] = result.inserted_id
    return note_helper(note_data)

@app.get("/notes/", response_model=list[schemas.NoteOut])
def get_all_notes():
    notes = list(notes_collection.find())
    return [note_helper(n) for n in notes]

@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
def get_note(note_id: str):
    note = notes_collection.find_one({"_id": ObjectId(note_id)})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note_helper(note)

@app.put("/notes/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: str, note_in: schemas.NoteUpdate):
    update_data = {k: v for k, v in note_in.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()

    result = notes_collection.update_one(
        {"_id": ObjectId(note_id)}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    updated_note = notes_collection.find_one({"_id": ObjectId(note_id)})
    return note_helper(updated_note)

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    result = notes_collection.delete_one({"_id": ObjectId(note_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
