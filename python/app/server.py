import fastapi


app = fastapi.FastAPI()


@app.get("/")
def index() -> str:
    return "yeet"
