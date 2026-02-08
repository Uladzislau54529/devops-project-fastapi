from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text

# --- Application ---
main = FastAPI(
    title="Project 2 API",
    version="1.0.0"
)

# --- Database configuration ---
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# --- Basic endpoints ---
@main.get("/")
def root():
    return {"message": "Project 2 is running"}

@main.get("/health")
def health():
    return {"status": "ok"}

# --- Database check endpoint ---
@main.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception as e:
        return {
            "database": "error",
            "details": str(e)
        }
