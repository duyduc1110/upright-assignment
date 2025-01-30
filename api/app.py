from fastapi import FastAPI, HTTPException
from typing import List
from contextlib import asynccontextmanager
from sqlalchemy import select
from dictionaries import SGD_LIST, IMPACT_LIST, PRODUCT_LIST
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from models import Base, Sgd, Impact, Product, CompanyRevenue
from schemas import SgdSchema, ImpactSchema, CompanyRevenueSchema
from schemas import ProductSchema, ProductCreateionSchema, ProductSimpleSchema
from db import SessionLocal, engine, get_db

async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        result = await conn.execute(select(Sgd))
        if result.first() is None:
            sgds = [Sgd(id=sgd["id"], name=sgd["name"]) for sgd in SGD_LIST]
            await conn.execute(Sgd.__table__.insert().values(
                [{"id": sgd.id, "name": sgd.name} for sgd in sgds]
            ))

        impact_result = await conn.execute(select(Impact))
        if impact_result.first() is None:
            impacts = [Impact(id=impact["id"], name=impact["name"]) for impact in IMPACT_LIST]
            await conn.execute(Impact.__table__.insert().values(
                [{"id": impact.id, "name": impact.name} for impact in impacts]
            ))

        product_result = await conn.execute(select(Product))
        if product_result.first() is None:
            products = [Product(
                id=product["id"],
                name=product["name"],
                sgd_id=product["sgd_id"],
                impact_id=product["impact_id"],
                parent_id=product["parent_id"]
            ) for product in PRODUCT_LIST]
            await conn.execute(Product.__table__.insert().values(
                [{"id": product.id, "name": product.name, "sgd_id": product.sgd_id, "impact_id": product.impact_id, "parent_id": product.parent_id} for product in products]
            ))
        

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_database()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"name": "Bruce"}

@app.get("/sgds/", response_model=List[SgdSchema])
async def read_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sgd))
    items = result.scalars().all()
    return items

@app.get("/impacts/", response_model=List[ImpactSchema])
async def read_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Impact))
    items = result.scalars().all()
    return items

@app.get("/products/", response_model=List[ProductSchema])
async def read_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    items = result.scalars().all()
    return items

@app.post("/products/", response_model=ProductSimpleSchema)
async def create_item(product: ProductCreateionSchema, db: AsyncSession = Depends(get_db)):
    try:
        new_product = Product(
            name=product.name,
            sgd_id=product.sgd_id,
            impact_id=product.impact_id,
            parent_id=product.parent_id
        )
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)
        return new_product
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/company_revenues/", response_model=List[CompanyRevenueSchema])
async def read_company_revenues(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CompanyRevenue))
    items = result.scalars().all()
    return items