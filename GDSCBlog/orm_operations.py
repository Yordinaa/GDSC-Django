# orm_operations.py
from django.db import models
from django.db.models import ArrayField
from BlogApp.models import Post
from CommentApp.models import Comment

# Post operations

# Create posts
post1 = Post.objects.create(title="Post 1", content="Content 1", category="Category 1")
post2 = Post.objects.create(title="Post 2", content="Content 2", category="Category 2")

# Query by category
posts = Post.objects.filter(category="Category 1")
print(posts)

# Update post
post1.content = "Updated content"
post1.save() 

# Delete post
post2.delete()


# Comment operations

# Create comments 
comment1 = Comment.objects.create(content="Comment 1", post=post1)
comment2 = Comment.objects.create(content="Comment 2", post=post1) 

# Query by post
comments = Comment.objects.filter(post=post1)
print(comments)

# Update comment
comment1.content = "Updated comment"
comment1.save()

# Delete comment 
comment2.delete()