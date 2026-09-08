from pydantic import BaseModel , EmailStr, Field

class UsersSignIN(BaseModel):
    name :str = Field(...)
    email : EmailStr
    password : str = Field(...)
    retypePass :str 
    is_active : bool = True

class UsersSignIN_response(BaseModel):
    id : int
    name :str = Field(...)
    email : EmailStr
    is_active : bool = True

class LoginData_check(BaseModel):
    email: EmailStr
    password : str
