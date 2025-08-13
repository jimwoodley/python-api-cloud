import fastapi from FastAPI

app = FastAPI()

@app.get('/hello')
def read_hello():
    return {"hello": "Hello, World!"}