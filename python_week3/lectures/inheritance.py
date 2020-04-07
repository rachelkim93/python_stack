from model import DatabaseModel

database = {
    "user": [],
    "post": [],
    "other": []
}

class User(DatabaseModel):
    def __init__(self, first_name, last_name):
        super().__init__()

    def save(self):
        database["user"].append(self)

class Post(DatabaseModel):
    def __init__(self, content, user_id):
        super().__init__()
        self.save = False

u=User("Rachel", "Kim")
u.save()

c=Comment("Great scott", 2)
c.save()

print(database)

p=Post()
p.save #overrode method in Post class from method to boolean so no parentheses 