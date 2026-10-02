from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "My Train Model backend is working!"
        }

@app.get("/train")
def train():
    return {
        "name": "My Train",
        "status": "active"
        }