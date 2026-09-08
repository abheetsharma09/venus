from sqlalchemy.orm import Session
from app.services.journalWork import get_journalContent , post_journalContent , delete_journalContent

def get_journalContent_controller(db :Session):
    return get_journalContent(db)

def post_journalContent_controller(db , user_data):
    return post_journalContent(db, user_data)

def delete_journalContent_controller(db , target_id):
    return delete_journalContent(db , target_id )