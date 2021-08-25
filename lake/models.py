from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Numeric

from sql_app.database import Base


class Lake(Base):
    __tablename__ = 'lake'

    id: int = Column(Integer, primary_key=True)
    temp_lake: float = Column(Numeric(precision=5, scale=2), nullable=False)
    temp_air: float = Column(Numeric(precision=5, scale=2), nullable=False)
    humidity_air: float = Column(Numeric(precision=5, scale=2), nullable=False)
    datetime: datetime = Column(DateTime, default=datetime.now, nullable=False)
