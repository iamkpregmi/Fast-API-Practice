from fastapi import FastAPI

app = FastAPI() #instance of fastapi

@app.get('/')
def index():

    # return "Welcome to the home page first"
    return {'data': 'Welcome to the home page'}


@app.get("/about")
def about():
    return {'data': 'Welcome to the about page'}


@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}

