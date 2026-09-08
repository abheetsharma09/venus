from sqlalchemy.orm import Session
from app.services.userWork import postUserdata_response ,postUserdata , delete_userData , checkLogin_users

def get_logged_users_controller(db: Session):
    return postUserdata_response(db) 

def create_user_controller(db, user_data):
    return postUserdata(db, user_data)

def delete_userData_controller(db , id):
    return delete_userData(db , id)

def checkLogin_users_controller(db , user_data):
    return checkLogin_users(db , user_data)
