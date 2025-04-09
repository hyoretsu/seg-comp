import os

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

engine = create_engine(os.getenv("DATABASE_URL"))

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False),
)

metadata_obj.create_all(engine)
