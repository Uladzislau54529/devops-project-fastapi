from fastapi import FastAPI

main = FastAPI()

@main.get("/")
def root():
    return {"message": "DevOps project is running"}

@main.get("/health")
def health():
    return {"status": "ok"}