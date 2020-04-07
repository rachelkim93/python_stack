from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wish(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name="posted_user")
    granted = models.ForeignKey(User, related_name="granted_wish")
    liked_by = models.ManyToManyField(User, related_name="liked_wishes", default="0")
    pending_wishes = models.ManyToManyField(User, related_name="wishes_pending")
    granted_wishes = models.ManyToManyField(User, related_name="wishes_granted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
