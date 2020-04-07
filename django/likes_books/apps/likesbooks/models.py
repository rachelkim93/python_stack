from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_by")
    liked = models.ManyToManyField(User, related_name="likes")


# which user liked the first book
# User.objects.filter(likes=Book.objects.get(id=1)).values()
# which users liked the second book
# User.objects.filter(likes=Book.objects.get(id=2)).values()

# which users uploaded the first book
# User.objects.filter(uploaded_by=Book.objects.get(id=1)).values()
# which user uploaded the second book
# User.objects.filter(uploaded_by=Book.objects.get(id=2)).values()

# User 1 upload book
# In [14]: book = Book.objects.create(title="Eat,Pray,Love", uploader=User.objects
#     ...: .get(id=1))                                                            


# User 1 likes book 1
# In [27]: this_user = User.objects.get(id=1)                                     

# In [28]: this_book = Book.objects.get(id=1)                                     

# In [29]: this_book.liked.add(this_user)  

# In [32]: this_book.liked.all()                                                  
# Out[32]: <QuerySet [<User: User object>]>

# In [33]: this_book.liked.count()                                                
# Out[33]: 1
