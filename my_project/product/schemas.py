from pydantic import BaseModel

class Product(BaseModel):
    name:str
    description:str
    price:int
    

# to display the required response 
class DisplayProduct(BaseModel):
    name:str
    description:str
    
    class Config():
        orm_mode = True
        