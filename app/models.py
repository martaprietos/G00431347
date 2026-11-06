from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class RequestDB(Base):
    __tablename__ ="requests"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    equipment_id: Mapped[int] =  mapped_column(Integer)
    student_id: Mapped[str] = mapped_column(String(9), unique= True, nullable=False)
    description: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String("OPEN"))