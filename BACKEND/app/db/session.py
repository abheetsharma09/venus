from sqlalchemy.orm import sessionmaker , declarative_base
from app.db.database import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine, checkfirst=True)

# FastAPI Dependency to handle opening and closing database sessions safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
