from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return 'Hello World from  FASTAPI '

@app.get('/property')
def property():
    return 'Hello World from Property FASTAPI page'

#id here is a path parameter
@app.get('/employeeID/{id}')
def employee(id):
    return {f'Employee id is {id}'}