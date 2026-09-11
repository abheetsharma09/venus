from fastapi import APIRouter , Depends
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.userModel import User
from app.controller.userWork import get_logged_users_controller , create_user_controller, delete_userData_controller , checkLogin_users_controller
from app.schemas.userSchema import UsersSignIN , UsersSignIN_response , LoginData_check

router = APIRouter()

@router.get('/api/get/signin/users/profile' , response_model=list[UsersSignIN_response])
def get_loggedUsers(db : Session = Depends(get_db)):
    # Call the updated controller function
    return get_logged_users_controller(db)

@router.post('/api/post/signin/users/profile') 
def post_userData(user_data: UsersSignIN, db: Session = Depends(get_db)):
    return create_user_controller(db, user_data)

@router.delete('/api/delete/signin/users/profile/{id}')
def delete_userData(id :int , db : Session = Depends(get_db)):
    return delete_userData_controller(db , id)
    
####### LOGIN AUTHENTICATION CODE ##########

@router.post('/api/get/login/users/check')
def login_userCheck(user_data:LoginData_check , db: Session = Depends(get_db)):
    return checkLogin_users_controller(db, user_data)