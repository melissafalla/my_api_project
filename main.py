import fastapi
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from routes.routes import router
from models import models
from database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
