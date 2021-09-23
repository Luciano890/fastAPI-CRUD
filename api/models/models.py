from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.schema import Table

from config.db import Base, conn, meta
from schemas.user import Post

    
users = Table("users",meta,
    Column("id",Integer,primary_key=True),
    Column("username", String(255)),
    Column("lastmessage",String(500)),
    Column("is_active",Boolean(False)))