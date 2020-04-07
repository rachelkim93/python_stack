class DatabaseModel:
    database = {}
    def __init__(self):
        self.id = 0

    def save(self):
        class_name = self.__class__.__name__
        if class_name in database:
            database[class_name].append(self)
        else:
            database[class_name] = []
            database[class_name].append(self)

    def update(self):
        print("Updating...")

    def print_my_type(self):
        class_name = self.__class__.__name__
        for i in database[class_name]:
            print(i)