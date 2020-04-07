from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField(max_length=1000)
    posted_by = models.ForeignKey(User, related_name="posted_quotes")
    liked_by = models.ManyToManyField(User, related_name="liked_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    commented_by = models.ForeignKey(User, related_name="commentor")
    commented_on = models.ForeignKey(Quote, related_name="posted_on")
