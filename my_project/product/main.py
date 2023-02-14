from fastapi import FastAPI
from .import models
from .database import engine
from sqlalchemy.sql.functions import mode
from .routers import product,seller,login



app = FastAPI(
     title="Product/Seller API",
     description="Get all the Product  description on API call",
     terms_of_service="http://www.google.com",
     contact={
         "Developer name": "Laxman Chowdary",
         "Website":"http://www.google.com",
         "email":"demo@gmaol.com",
     },
     license_info= {
         'name': "ABC",
         "url":"http://www.google.com"
     },
    #  docs_url="/documentation",
    #  redoc_url=None,
)
app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)


models.Base.metadata.create_all(engine)






    





