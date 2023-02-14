from fastapi import APIRouter,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from ..database import get_db
from ..import schemas
from ..import models



router = APIRouter(
    tags=['Product'],
    prefix="/product"
)


#fetching all products
@router.get('/',status_code=status.HTTP_200_OK ,response_model= List[schemas.DisplayProduct])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
     



#fetching product by id
@router.get('/{id}', response_model=schemas.DisplayProduct)
def get_product(id, db:Session = Depends(get_db)):
    if (
        product := db.query(models.Product)
        .filter(models.Product.id == id)
        .first()
    ):
        return product
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Product not found with the Input Id')



#delete product from DB
@router.delete('/{id}')
def delete(id,db:Session = Depends(get_db)):
    delete_product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Product got deleted'}



#update product in DB
@router.put('/{id}')
def update(id, request:schemas.Product, db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {'Product got updated'}



#insert/post data into DB
@router.post('/',status_code=status.HTTP_201_CREATED)
def add(request:schemas.Product, db: Session = Depends(get_db)):
    db_product = models.Product(name = request.name, description = request.description,
                                 price = request.price, seller_id = 1)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product