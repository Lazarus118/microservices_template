from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
products = Table('products', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('food', VARCHAR(length=64)),
    Column('drink', VARCHAR(length=64)),
    Column('amount', VARCHAR(length=64)),
    Column('actual_food_amount', VARCHAR(length=64)),
    Column('location', VARCHAR(length=64)),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=20)),
    Column('password', VARCHAR(length=64)),
    Column('social_id', VARCHAR(length=64)),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=64)),
    Column('user_points', VARCHAR(length=1000)),
)

api = Table('api', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('status', String(length=512)),
    Column('meta_data', String(length=512)),
    Column('data', String(length=512)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['products'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['api'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['products'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['api'].drop()
