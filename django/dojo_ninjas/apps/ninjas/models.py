from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField()

class Ninja(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
