from sqlalchemy.orm import session
from app.models.userModel import User
from typing import Annotated
from fastapi import HTTPException ,status , Depends
from fastapi.security import OAuth2PasswordBearer
from app.services.security.hash import get_password_hash , verify_password
from app.services.security.jwt import create_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def postUserdata_response(db , token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = db.query(User).filter(User.email == user_data.email).first()
    token = create_access_token({'sub' : user.id})
    
    if not user:
        raise HTTPException(status_code=404, detail=f"{user_data.email} not found")
    else:
        if verify_password(user_data.password , user.password):
            return {
                "token_type": "bearer",
                "access_token": token,
                "msg": "LOGGED IN SUCCESS!!",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="INCORRECT PASSWORD!!"
            )