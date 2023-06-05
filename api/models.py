from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=200)
    address = models.JSONField(null=True)
    company = models.JSONField(null=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
