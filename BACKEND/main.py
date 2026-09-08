from fastapi import FastAPI
from app.routes.userRoute import router as signINroutes
from app.routes.journalRoute import router as journalRoute
from app.db.session import Base
from fastapi.middleware.cors import CORSMiddleware
# from app.db.database import engine
# from app.schemas.userSchema import UsersSignIN , UsersSignIN_response

# Base.metadata.create_all(engine)

app = FastAPI(title='Venus')

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signINroutes)
app.include_router(journalRoute)