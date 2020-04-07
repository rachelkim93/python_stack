from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class UserManager(models.Manager):

    def validate(request, postdata):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        print ("validate")
        print (postdata)
        if (not postdata['first_name'].isalpha() or len(postdata['first_name']) <= 0):
            errors['first_name'] = "Error: First Name needs to be alpha characters and cannot be empty"
        if (not postdata['last_name'].isalpha() or len(postdata['last_name']) <= 0):
            errors['last_name'] = "Error: Last Name needs to be alpha characters and cannot be empty"
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Error: Email format is incorrect"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __unicode__(self):
        return " id: " + str(self.id) + " fname: " + self.first_name + " lname: " + self.last_name + " email: " + self.email

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     desc = models.CharField(max_length=1000)
#     uploader = models.ForeignKey(User, related_name="uploaded_books")
#     liked_users = models.ManyToManyField(User, related_name="liked_books")    
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     def __unicode__(self):
#         return " id: " + str(self.id) + " name: " + self.name + " desc: " + self.desc