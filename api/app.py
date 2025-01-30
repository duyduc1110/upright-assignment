from fastapi import FastAPI, HTTPException
from typing import List
from contextlib import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.orm import joinedload, subqueryload, selectinload
from dictionaries import SGD_LIST, IMPACT_LIST, PRODUCT_LIST, COMPANY_LIST, REVENUE_LIST
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from models import Base, Sgd, Impact, Product, Revenue, Company
from schemas import SgdSchema, ImpactSchema
from schemas import ProductSchema, ProductCreateionSchema, ProductSimpleSchema
from schemas import RevenueSingleCompanySchema
from db import engine, get_db

import json
import pandas as pd


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        result = await conn.execute(select(Sgd))
        if result.first() is None:
            sgds = [Sgd(id=sgd["id"], name=sgd["name"]) for sgd in SGD_LIST]
            await conn.execute(Sgd.__table__.insert().values(
                [{"id": sgd.id, "name": sgd.name} for sgd in sgds]
            ))

            impacts = [Impact(id=impact["id"], name=impact["name"]) for impact in IMPACT_LIST]
            await conn.execute(Impact.__table__.insert().values(
                [{"id": impact.id, "name": impact.name} for impact in impacts]
            ))

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

            companies = [Company(id=company["id"], name=company["name"]) for company in COMPANY_LIST]
            await conn.execute(Company.__table__.insert().values(
                [{"id": company.id, "name": company.name} for company in companies]
            ))

            revenues = [Revenue(id=revenue["id"], company_id=revenue["company_id"], product_id=revenue["product_id"], gmv=revenue["gmv"]) for revenue in REVENUE_LIST]
            await conn.execute(Revenue.__table__.insert().values(
                [{"id": revenue.id, "company_id": revenue.company_id, "product_id": revenue.product_id, "gmv": revenue.gmv} for revenue in revenues]
            ))
        

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_database()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/sgds/", response_model=List[SgdSchema])
async def get_all_sgds(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sgd))
    items = result.scalars().all()
    return items

@app.get("/impacts/", response_model=List[ImpactSchema])
async def get_all_impacts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Impact))
    items = result.scalars().all()
    return items

@app.get("/products/", response_model=List[ProductSchema])
async def get_all_products(db: AsyncSession = Depends(get_db)):
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

@app.get("/revenues/{company_id}")
async def get_company_revenue(company_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Revenue)
        .options(
            joinedload(Revenue.product)
            .joinedload(Product.parent)
            .joinedload(Product.parent)
            .joinedload(Product.parent)
        )
        .where(Revenue.company_id == company_id)
    )
    items = result.unique().scalars().all()

    return [
        {
            "id": item.id,
            "product_id": item.product_id,
            "name": item.product.name,
            "sgd_id": item.product.possible_sgd_id,
            "impact_id": item.product.possible_impact_id,
            "gmv": item.gmv,
        }
        for item in items
    ]

@app.get("/reports/{company_id}")
async def get_company_revenue(company_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Revenue)
        .options(
            joinedload(Revenue.product)
            .joinedload(Product.parent)
            .joinedload(Product.parent)
            .joinedload(Product.parent)
        )
        .where(Revenue.company_id == company_id)
    )
    items = result.unique().scalars().all()

    df = pd.DataFrame([
        {
            "sgd_id": item.product.possible_sgd_id,
            "impact_id": item.product.possible_impact_id,
            "gmv": item.gmv,
        }
        for item in items
    ])

    sgds_result = await db.execute(select(Sgd))
    df_sgd = pd.DataFrame([
        {"id": sgd.id, "name": sgd.name}
        for sgd in sgds_result.scalars().all()
    ]).rename(columns={"id": "sgd_id", "name": "sgd_name"})

    impacts_result = await db.execute(select(Impact))
    df_impact = pd.DataFrame([
        {"id": impact.id, "name": impact.name}
        for impact in impacts_result.scalars().all()
    ]).rename(columns={"id": "impact_id", "name": "impact_name"})

    result_df = df.groupby(['sgd_id', 'impact_id'])['gmv'].sum().reset_index()\
        .merge(df_sgd, on='sgd_id', how='left')\
        .merge(df_impact, on='impact_id', how='left')

    return result_df.to_dict('records')