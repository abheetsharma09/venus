from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped , mapped_column 
from sqlalchemy.sql import func
from app.models.userModel import User
from app.db.session import Base

class Journal(Base):
    __tablename__ = "journal"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    # This creates a TEXT column in PostgreSQL with no length limit
    description: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
