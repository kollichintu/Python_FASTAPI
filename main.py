from fastapi import FastAPI,Form

app = FastAPI()


@app.get('/')
def hello():
    return 'Hello World from  FASTAPI '

@app.get('/property')
def property():
    return 'Hello World from Property FASTAPI page'

#id here is a path parameter
@app.get('/employeeID/{id}')
def employee(id: int):
    return {f'Employee id is {id}'}

@app.get('/profile/admin')
def profile():
    return {'This is admin profile page'}

@app.get('/profile/{username}')
def profile(username):
    return {f'This is profile page from {username}'}

#query paramater
#products?id=value
@app.get('/products')
def products(id=9,price=500):
    return {f'The product id is {id} and price is {price}'}


@app.post('/login')
def login(userName:str = Form(...), password:str = Form(...)):
    return {"UserName is": userName}
    





