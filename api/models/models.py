from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Date, Text

from config.db import Base, conn, meta, engine
from schemas.user import Post

    
users = Table("users",meta,
            Column("id",Integer,primary_key=True),
            Column("username", String(255)),
            Column("lastmessage",Text),
            Column("is_active",Boolean(False))
            )

datas = Table("datas",meta,
            Column("id",Integer,primary_key=True),
            Column("username",String(255)),
            Column("message_date",Date),
            Column("view_at",DateTime),
            Column("published",Boolean(False)),
            Column("message",Text),
            )

meta.create_all(engine)