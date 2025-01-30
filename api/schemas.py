from pydantic import BaseModel
from typing import List, Optional

class SgdSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ImpactSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ProductSchema(BaseModel):
    id: int
    name: str
    sgd_id: int
    impact_id: int
    parent_id: Optional[int] = None
    sgd: SgdSchema
    impact: ImpactSchema
    parent: Optional['ProductSchema'] = None
    children: List['ProductSchema'] = []

    class Config:
        from_attributes = True

class ProductCreateionSchema(BaseModel):
    name: str
    sgd_id: Optional[int] = None
    impact_id: Optional[int] = None
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True

class ProductSimpleSchema(BaseModel):
    id: int
    name: str
    impact_id: Optional[int] = None
    sgd_id: Optional[int] = None
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True

class RevenueSchema(BaseModel):
    id: int
    company_id: int
    product_id: int
    gmv: float

    class Config:
        from_attributes = True

class RevenueSingleCompanySchema(BaseModel):
    id: int
    gmv: float
    product: ProductSimpleSchema

    class Config:
        from_attributes = True

ProductSchema.model_rebuild()