from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app=FastAPI()


@app.get("/")
def root():
    return {"message": "Hey There! Welcome to the API!"}

@app.get("/posts")
def get_posts():
    return {"data":"Hey There!These are your posts!"}

@app.post("/createpost")
def create_post(payload: dict= Body(...)):
    return {"New post":f"Title :{payload['title']} Content: {payload['content']}"}