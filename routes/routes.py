from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import models
from controllers import movies_controller
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = movies_controller.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.get("/movies/")
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    movies = movies_controller.get_movies(db)
    return movies

@router.post("/movies/")
def create_movie(movie: models.Movie, db: Session = Depends(get_db)):
    return movies_controller.create_movie(db=db, movie=movie)

@router.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: models.Movie, db: Session = Depends(get_db)):
    db_movie = movies_controller.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies_controller.update_movie(db, movie_id, movie.dict())

@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = movies_controller.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies_controller.delete_movie(db, movie_id=movie_id)
