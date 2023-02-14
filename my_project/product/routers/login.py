from fastapi import APIRouter, status, HTTPException, Depends
from ..import schemas, models, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..database import get_db
from passlib.context import CryptContext

router = APIRouter(
    tags=['User']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


@router.post('/login')
def login(request:schemas.Login,  db:Session = Depends(get_db)):
    
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='User not found')
    
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='Password is incorrect')
    
    return request