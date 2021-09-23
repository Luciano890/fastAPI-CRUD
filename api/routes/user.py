from uuid import uuid4

from fastapi import APIRouter, HTTPException, Response, status
from starlette import status
from starlette.status import HTTP_204_NO_CONTENT
from models.models import Post

from models.models import users
from config.db import conn
from schemas.user import User

user = APIRouter()

posts = []


@user.get("/users", response_model=list[User], tags=["users"])
async def get_users():
    return conn.execute(users.select()).fetchall()


@user.get("/users/{id}", response_model=User, tags=["users"])
async def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.post("/users", response_model=User, tags=["users"])
async def create_users(user: User):
    new_user = {"username": user.username,
                "lastmessage": user.lastmessage, "is_active": user.is_active}
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.delete("/users/{id}", status_code=status, tags=["users"])
async def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, updateUser: User):
    conn.execute(users.update().values(username=updateUser.username,
                 lastmessage=updateUser.lastmessage, is_active=updateUser.is_active).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.get("/", tags=["chat"])
async def read_root():
    return {"welcome": "API chat running"}


@user.get("/posts", tags=["chat"])
async def get_posts():
    return posts[:]


@user.get("/posts/{post_id}", tags=["chat"])
async def get_post_id(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(status_code=404, detail="Post not found")


@user.post("/posts", tags=["chat"])
async def set_post(post: Post):
    post.id = str(uuid4())
    posts.append(post.dict())
    return posts[-1]


@user.delete("/posts/{post_id}", tags=["chat"])
async def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been delete successfully"}

    raise HTTPException(status_code=404, detail="Post not found")


@user.put("/posts/{post_id}", tags=["chat"])
async def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["model"] = updatePost.model
            posts[index]["fields"]["data"]["username"] = updatePost.fields.data.username
            posts[index]["fields"]["data"]["message_date"] = updatePost.fields.data.message_date
            posts[index]["fields"]["data"]["view_at"] = updatePost.fields.data.view_at
            posts[index]["fields"]["data"]["published"] = updatePost.fields.data.published
            posts[index]["fields"]["data"]["message"] = updatePost.fields.data.message

            return {"message": "Post has been update successfully"}

    raise HTTPException(status_code=404, detail="Post not found")
