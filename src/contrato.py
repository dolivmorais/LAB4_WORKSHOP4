from pydantic import BaseModel,EmailStr,PositiveFloat,PositiveInt,field_validator
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum  

    @field_validator("categoria")
    def categoria_enum(cls,error):
        return error