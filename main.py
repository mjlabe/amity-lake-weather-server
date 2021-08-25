from fastapi import FastAPI, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session

from sql_app.database import SessionLocal
from lake.models import Lake

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/lake")
async def get_lake_weather(page: int, limit: int, db: Session = Depends(get_db)):
    if page and limit:
        page = 1 if page < 1 else page
        print(db.query(Lake).order_by(desc(Lake.datetime)).all())
        return db.query(Lake).order_by(desc(Lake.datetime)).offset((page - 1) * limit).limit(limit).all()
    db.query(Lake).order_by(desc(Lake.id)).first()


@app.post("/lake")
async def save_lake_weather(data: dict, db: Session = Depends(get_db)):
    lake_obj = Lake(
        temp_lake=data['temp_lake'],
        temp_air=data['temp_air'],
        humidity_air=data['humidity_air'],
    )
    db.add(lake_obj)
    db.commit()
    db.refresh(lake_obj)
    return lake_obj
