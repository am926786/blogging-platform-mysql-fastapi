from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='blog',
    cursorclass=pymysql.cursors.DictCursor
)

print("MySQL connection established successfully!")

class Post(BaseModel):
    title: str
    content: str

class Comment(BaseModel):
    post_id: int
    text: str

class LikeDislike(BaseModel):
    post_id: int
    like: bool

app = FastAPI()

@app.post("/posts/")
def create_post(post: Post):
    with connection.cursor() as cursor:
        sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        cursor.execute(sql, (post.title, post.content))
        connection.commit()
        return {"message": "Post created successfully"}

@app.get("/posts/")
def get_posts():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM posts"
        cursor.execute(sql)
        posts = cursor.fetchall()
        return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM posts WHERE id = %s"
        cursor.execute(sql, (post_id,))
        post = cursor.fetchone()
        if post:
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    with connection.cursor() as cursor:
        sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
        cursor.execute(sql, (post.title, post.content, post_id))
        connection.commit()
        return {"message": "Post updated successfully"}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    with connection.cursor() as cursor:
        sql = "DELETE FROM posts WHERE id = %s"
        cursor.execute(sql, (post_id,))
        connection.commit()
        return {"message": "Post deleted successfully"}

@app.post("/comments/")
def create_comment(comment: Comment):
    with connection.cursor() as cursor:
        sql = "INSERT INTO comments (post_id, text) VALUES (%s, %s)"
        cursor.execute(sql, (comment.post_id, comment.text))
        connection.commit()
        return {"message": "Comment created successfully"}

@app.post("/likes_dislikes/")
def like_dislike_post(like_dislike: LikeDislike):
    with connection.cursor() as cursor:
        sql = "INSERT INTO likes_dislikes (post_id, is_like) VALUES (%s, %s)"
        cursor.execute(sql, (like_dislike.post_id, like_dislike.like))
        connection.commit()
        return {"message": "Like/Dislike recorded successfully"}

@app.get("/comments/{post_id}")
def get_comments(post_id: int):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM comments WHERE post_id = %s"
        cursor.execute(sql, (post_id,))
        comments = cursor.fetchall()
        return comments
