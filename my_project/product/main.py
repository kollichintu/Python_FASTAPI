from fastapi import FastAPI,status,HTTPException
from fastapi.params import Depends
from .import schemas
from .import models
from .database import engine,SessionLocal
from sqlalchemy.sql.functions import mode
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#fetching all products
@app.get('/products',status_code=status.HTTP_200_OK ,response_model= List[schemas.DisplayProduct])
def get_products(db: Session = Depends(get_db)):
    all_products = db.query(models.Product).all()
    return all_products



#fetching product by id
@app.get('/product/{id}',response_model=schemas.DisplayProduct)
def get_product(id, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Product not found with the Input Id')
    return product



#delete product from DB
@app.delete('/product/{id}')
def delete(id,db:Session = Depends(get_db)):
    delete_product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Product got deleted'}



#update product in DB
@app.put('/product/{id}')
def update(id, request:schemas.Product, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {'Product got updated'}



#insert/post data into DB
@app.post('/product',status_code=status.HTTP_201_CREATED)
def add(request:schemas.Product, db: Session = Depends(get_db)):
    db_product = models.Product(name = request.name, description = request.description,
                                 price = request.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    
