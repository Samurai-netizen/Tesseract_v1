from sqlalchemy import create_engine
from sqlalchemy import insert, select
from pymysql import connect
from Database.DB_schemes import goods, metadata
import uvicorn
from fastapi import FastAPI

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import asyncio

from config import MYSQL_ADDRESS

print("DB_Conn.py is running")

engine = create_engine(MYSQL_ADDRESS)  # , echo=True

metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

async def DB_test() -> None:

    with engine.connect() as connection:
        try:
            insert_query = insert(goods).values(id=3, article='NEWITEM', amount=77, buy_price_rmb=2000, margin=24.4)
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


async def db_insert(article, amount, sku):  #id=3, article='DOMB', amount=77, buy_price_rmb=2000, margin=24.4

    print("data_to_insert", article, amount, sku)

    data_to_insert = {
        'id': sku,
        'article': article,
        'amount': amount
    }

    required_fields = ["article", "amount", "id"]
    for field in required_fields:
        if field not in data_to_insert or not data_to_insert[field]:
            print(f"Отсутствует обязательное поле: {field}")
            return "error"

    with engine.connect() as connection:
        try:
            insert_query = insert(goods)
            connection.execute(insert_query, data_to_insert)
            connection.commit()
            print("Inserted")
        except Exception as e:
            print(f"Insert failure: {e}")

    return "done"

async def db_update(*args):  #id=3, article='DOMB', amount=77, buy_price_rmb=2000, margin=24.4

    print("data_to_insert", args[0], args[1],args[2])

    data_to_insert = {
        'id': args[2],
        'article': args[0],
        'amount': args[1]
    }

    required_fields = ["article", "amount", "id"]
    for field in required_fields:
        if field not in data_to_insert or not data_to_insert[field]:
            print(f"Отсутствует обязательное поле: {field}")
            return "error"

    with engine.connect() as connection:
        try:
            insert_query = insert(goods)
            connection.execute(insert_query, data_to_insert)
            connection.commit()
            print("Inserted")
        except Exception as e:
            print(f"Insert failure: {e}")

    return "done"

if __name__ == "__main__":
    asyncio.run(DB_test())
