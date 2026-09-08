from sqlalchemy.orm import session
from app.models.userModel import User
from fastapi import HTTPException ,status
from app.services.security.security import get_password_hash , verify_password

def postUserdata_response(db):
    users = db.query(User).all()
    return users

def postUserdata(db, user_data):
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=get_password_hash(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return HTTPException(
        status_code=status.HTTP_201_CREATED, 
        detail=f"User created sucessfully!!"
    )


def delete_userData(db, id :int):
    db_item = db.query(User).filter(User.id == id).first()
    
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Item with id {id} not found"
        )
    
    db.delete(db_item)
    db.commit()
    
    return None

def checkLogin_users(db ,user_data):
    pass