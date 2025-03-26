print("hello")

from sqlalchemy import create_engine
from sqlalchemy import insert, select
from pymysql import connect
from Database.DB_schemes import goods, metadata
import uvicorn
from fastapi import FastAPI

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import asyncio

async def DB_test() -> None:

    engine = create_engine('mysql+pymysql://freedb_SamuraiDev:ymBquG!QmPreX2!@sql.freedb.tech:3306/freedb_warehouse')  # , echo=True

    metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    app = FastAPI()

    with engine.connect() as connection:
        try:
            insert_query = insert(goods).values(id=3, article='DOMB', amount=77, buy_price_rmb=2000, margin=24.4)
            connection.execute(insert_query)
            connection.commit()
            print("inserted")
        except:
            print("Insert failure")

    with engine.connect() as connection:
        try:
            select_query = select(goods)
            result = connection.execute(select_query)
            for row in result.mappings():
                print(row)
            print("selected")
        except:
            print("Select failure")

    """
    # Read (GET)
    @app.get(&quot;/items/{item_id}&quot;)
    async def read_item(item_id: int):
        db = SessionLocal()
        item = db.query(Item).filter(Item.id == item_id).first()
        return item
    
    """


if __name__ == "__main__":
    asyncio.run(DB_test())
