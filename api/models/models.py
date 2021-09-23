from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

from config.db import Base, conn, meta, engine
from schemas.user import Post

    
users = Table("users",meta,
    Column("id",Integer,primary_key=True),
    Column("username", String(255)),
    Column("lastmessage",String(500)),
    Column("is_active",Boolean(False)))

meta.create_all(engine)
