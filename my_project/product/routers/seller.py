from fastapi import APIRouter,status
from typing import List
from ..import schemas
from ..import models
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from passlib.context import CryptContext


router = APIRouter(
    tags=['Seller'],
    prefix="/seller"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#fetching all sellers
@router.get('/',status_code=status.HTTP_200_OK ,response_model= List[schemas.DisplaySeller])
def get_sellers(db: Session = Depends(get_db)):
    return db.query(models.Seller).all()



@router.post('/',response_model=schemas.DisplaySeller)
def create_seller(request:schemas.Seller, db:Session = Depends(get_db)):
    hash_password = pwd_context.hash(request.password)
    db_seller = models.Seller(username = request.username, email = request.email, password = hash_password)
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    
    return db_seller


@router.delete('/{id}')
def delete(id,db:Session = Depends(get_db)):
    delete_seller = db.query(models.Seller).filter(models.Seller.id == id).delete(synchronize_session=False)
    db.commit()
    return {'seller got deleted'}