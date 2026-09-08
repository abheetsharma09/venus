from fastapi import APIRouter , Depends
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.journalModel import Journal
from app.schemas.journalSchema import JournalLOG , JournalResponse
from app.controller.journalWorker import get_journalContent_controller , post_journalContent_controller , delete_journalContent_controller

router = APIRouter()

@router.get('/api/get/journals' , response_model=list[JournalResponse])
def get_journal(db:Session = Depends(get_db)):
    return get_journalContent_controller(db)

@router.post('/api/post/journals')
def post_journal(user_data: JournalLOG, db: Session = Depends(get_db)):
    return post_journalContent_controller(db, user_data)

@router.delete('/api/delete/journal/{id}')
def delete(id :int , db: Session= Depends(get_db)):
    return delete_journalContent_controller(db , id)
