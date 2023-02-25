from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str


posts: list[Post] = []


@app.get('/posts')
def get_posts() -> list[Post]:
    return posts


@app.post('/posts')
def create_post(post: Post):
    posts.append(post)
    return {
        "message": "Successfully post created!",
        "posts": posts
    }


@app.put('/posts')
def update_post(upost: Post):
    post = [p for p in posts if p.id == upost.id]
    if len(post) > 0:
        post = post[0]
        posts.remove(post)
        post.title = upost.title
        posts.append(post)
        return {
            "message": "post has been updated",
            "posts": posts
        }

    return {
        "message": "The post does'nt exists!"
    }


@app.delete('/posts/{id}')
def delete_post(id: int):
    global posts
    posts = [p for p in posts if p.id != id]
    return {
        "message": "The post has been deleted.",
        "posts": posts
    }


@app.get('/posts/{id}')
def get_post(id: int):
    filtered_posts = [p for p in posts if p.id == id]
    if filtered_posts:
        return {
            "post": filtered_posts[0]
        }
    return {
        "post": []
    }
