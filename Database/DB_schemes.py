from sqlalchemy import Table, Column, Integer, Float, String, MetaData, VARCHAR

metadata = MetaData()

goods = Table(
    'goods', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('article', VARCHAR(10), primary_key=True),
    Column('amount', Integer),
    Column('buy_price_rmb', Float),
    Column('margin', Float)
)
