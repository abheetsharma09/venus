from pydantic import BaseModel

class JournalLOG(BaseModel):
    title : str
    description : str
    user_id : int

class JournalResponse(BaseModel):
    id : int
    title :str
    description: str
    user_id : int
