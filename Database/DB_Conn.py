print("hello")

from sqlalchemy import create_engine
from sqlalchemy import insert, select
from pymysql import connect
from DB_schemes import goods, metadata
import uvicorn
from fastapi import FastAPI

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://freedb_SamuraiDev:ymBquG!QmPreX2!@sql.freedb.tech:3306/freedb_warehouse')  # , echo=True

metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

with engine.connect() as connection:
    try:
        insert_query = insert(goods).values(id=2, article='AMF1B', amount=15, buy_price_rmb=1000, margin=14.9)
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