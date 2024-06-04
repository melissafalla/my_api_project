from ..models.models import Movie
from ..database import SessionLocal

def get_movies():
    session = SessionLocal()
    movies = session.query(Movie).all()
    session.close()
    return movies

def get_movie(movie_id: int):
    session = SessionLocal()
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    session.close()
    return movie

def create_movie(movie):
    session = SessionLocal()
    session.add(movie)
    session.commit()
    session.refresh(movie)
    session.close()
    return movie

def update_movie(movie_id: int, movie_data):
    session = SessionLocal()
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        for key, value in movie_data.items():
            setattr(movie, key, value)
        session.commit()
        session.refresh(movie)
    session.close()
    return movie

def delete_movie(movie_id: int):
    session = SessionLocal()
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
    session.close()
    return movie
