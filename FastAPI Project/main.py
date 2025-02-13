from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
# from . import models
import models
from database import engine

app = FastAPI()

#this is the home page method
@app.get("/")
def home():
    return "Welcome to the Home Page!"


#this is the about page method
@app.get('/about')
def about():
    return {'data': 'Welcome to the about page'}


#this is the blog page method with validaton
@app.get('/blog/{id}')
def blog(id:int):
    return {'data': id}


#this is the blog comments page method
@app.get('/blog/{id}/comments')
def comments():
    return {'data': {'1','2'}}



#this is the post method for the sent data
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog:Blog):
    # return {'data': f"blog is created with title as {blog.title}"}
    return blog


#this is the delete blog method
@app.delete('/delete_blog/{id}')
def delete_blog(id):
    return {'data': f'Blog delete successfully {id}'}



models.Base.metadata.create_all(engine)