from datetime import datetime, timedelta, date
from uuid import uuid4

from pydantic import BaseModel
from typing import Optional, Text

class User(BaseModel):
    id: Optional[str]
    username: str
    lastmessage: Text
    is_active: bool = True
     
class Data(BaseModel):
    id: Optional[str]
    username: str = "user123"
    message_date: date
    view_at: Optional[datetime] = datetime.now()
    published: bool = False
    message: Text = "message text."
    
class Fields(BaseModel):
    data: Data

# Post Model
class Post(BaseModel):
    id: Optional[str]
    model: Optional[str] = "chat"
    fields: Fields      