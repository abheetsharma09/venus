from fastapi import FastAPI , HTTPException , status
from pydantic import BaseModel
import datetime
import json
from fastapi.params import Body
from typing import Optional, List
import psycopg2
import socket
from psycopg2.extras import RealDictCursor

try:
    #Database configurations
    connection = psycopg2.connect(host='localhost', database='fastapi_db' ,user='postgres' ,password='admin@123' , cursor_factory=RealDictCursor) 

    #Connection b/w db and py
    cursor = connection.cursor() #Used to run the SQL query from here

except Exception as err:
    print(f'ERROR!!!...{err}')

app = FastAPI()

class PostSignIN(BaseModel):
    name :str
    email : str
    password : str
    retypePass :str
    is_active : bool = True

@app.get('/api/get')
def home():
    #Executing Commands
    cursor.execute("""SELECT * FROM users;""")
    userData = cursor.fetchall()
    return userData

@app.post('/api/post')
def postData(payload : PostSignIN):
    # cursor.execute(f"INSERT INTO users (name, email, password, is_active) VALUES({payload.name} , {payload.email} , {payload.password} , {payload.is_active})") #Using this will cause sql injection we have to first santizize the data

    #Santitizing data first[using %]
    cursor.execute(
        """INSERT INTO users (name, email, password, is_active) VALUES (%s , %s , %s , %s) RETURNING *""" ,
        (payload.name , payload.email, payload.password , payload.is_active)
        )
    
    addUser_msg = cursor.fetchone()
    connection.commit()
git status

    return addUser_msg

#Path Parameter gives out the string type variable 
@app.get('/api/path/fetch/{id}')
def checkUser(id: int):
    cursor.execute("""SELECT * FROM users WHERE id = %s;""", (int(id),))

    selectedUser = cursor.fetchone()
    if not selectedUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User not Found with id Provided"
        )

    return selectedUser

@app.delete('/api/delete/{id}')
def delUser(id: int):
    cursor.execute("""DELETE FROM users WHERE id = %s RETURNING *;""", (id,))
    
    dbResDel = cursor.fetchone()
    connection.commit() # Don't forget to commit your changes!
    
    if not dbResDel:
        raise HTTPException(status_code=404, detail="User not found")
        
    return dbResDel
    