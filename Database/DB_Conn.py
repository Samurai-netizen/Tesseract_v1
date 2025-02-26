print("hello")

from sqlalchemy import create_engine
from sqlalchemy import insert
import pymysql
from DB_schemes import goods, metadata

engine = create_engine('mysql+pymysql://if0_38402556:1296test@sql109.infinityfree.com/if0_38402556_warehouse')

metadata.create_all(engine)

insert_query = insert(goods).values(article='AMF1W', amount=30, buy_cost=1000, margin=14.8)
with engine.connect() as connection:
    connection.execute(insert_query)
