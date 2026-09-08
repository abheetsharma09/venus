from sqlalchemy.orm import session
from app.models.journalModel import Journal
from sqlalchemy import delete
from fastapi import HTTPException, status

#Get alll the DB
def get_journalContent(db):
    return db.query(Journal).all()

#Post the Journal in the DB
def post_journalContent(db ,user_data):
    new_journal = Journal(
        title= user_data.title,
        description= user_data.description,
        user_id=user_data.user_id
    )

    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)

    return HTTPException(
        status_code=status.HTTP_201_CREATED, 
        detail=f"Journal added sucessfully!!"
    )

#TO delete the USER
def delete_journalContent(db , target_id):
    # Construct the delete statement
    stmt = delete(Journal).where(Journal.id == target_id)
        
    # Execute and commit
    db.execute(stmt)
    db.commit()
    
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT, 
        detail=f"Journal deleted sucessfully!!"
    )
