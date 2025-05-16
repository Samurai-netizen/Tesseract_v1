from sqlalchemy import Table, Column, Integer, Float, String, MetaData, VARCHAR, Boolean, Date

metadata = MetaData()

goods = Table(
    'goods', metadata,
    Column('id', Integer),
    Column('article', VARCHAR(10), primary_key=True),
    Column('amount', Integer),
    Column('buy_price_rmb', Float),
    Column('margin', Float)
)

orders = Table(
    'orders', metadata,
    Column('order_id', Integer, primary_key=True, autoincrement=True),
    Column('name', VARCHAR(50)),
    Column('amount', Integer),
    Column('price_rmb_1pcs', Float),
    Column('price_rmb_total', Float),
    Column('if_paid', Boolean),
    Column('date_paid', Date),
    Column('date_china_arrival', Date),
    Column('shipment_id', Integer),
    Column('total_mass_kg', Float),
    Column('estimated_arrival', Date),
    Column('fact_arrival', Date),
    Column('if_picked_up', Boolean),
    Column('if_problems', Boolean)
)

shipments = Table(
    'shipments', metadata,
    Column('shipment_id', Integer, primary_key=True, autoincrement=True),
    Column('total_mass_kg', Float),
    Column('estimated_arrival', Date),
    Column('fact_arrival', Date),
    Column('total_cost_usdt', Float),
    Column('if_paid', Boolean),
    Column('if_picked_up', Boolean),
    Column('date_picked_up', Date),
    Column('if_problems', Boolean),
    Column('goods_names', VARCHAR(250))
)