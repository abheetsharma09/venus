from pydantic import BaseModel , EmailStr, Field
from typing import Optional

class UsersSignIN(BaseModel):
    name :str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)
    retypePass :Optional[str] 
    is_active : Optional[bool] = True

class UsersSignIN_response(BaseModel):
    id : int
    name :str = Field(...)
    email : EmailStr
    is_active : bool = True

class LoginData_check(BaseModel):
    email: EmailStr
    password : str
