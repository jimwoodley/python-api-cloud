from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get('/hello')
def read_hello():
    return {"hello": "Hello, World!"}

users = [
    User(id=1, name='James', email='james@example.com'),
    User(id=2, name='Naomi', email='naomi@example.com')
]