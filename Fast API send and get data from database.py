from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/test')
def test():
    return {'data': 'Test Successfully.'}


class Blog(BaseModel):
    title: str
    body: str
    is_published: Optional[bool]


#post blog to the database
@app.post('/blog')
def create_blog(request:Blog, db : Session = Depends(get_db)):
    # return {'data': f"blog is created with title as {blog.title}"}
    # return blog

    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#get all blogs from database
@app.get('/boog')
def all_blog(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


#get single blog form the database
@app.get('/single_blog/{id}')
def single_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

