def first_function(param_one):
    return 5
    print(param_one)

return_value = first_function("Hello")

print("Return value is {}".format(return_value))

###################

database = []


def registration(first_name, last_name, email, password):
    register_dictionary = {}
    register_dictionary['first_name'] = first_name
    register_dictionary['last_name'] = last_name
    register_dictionary['email'] = email
    register_dictionary['password'] = password
    return register_dictionary

def get_user_info():
    first = input("First name: \n")
    last = input("Last name: \n")
    email = input("Email: \n")
    password = input("Password: \n")

    db_entry = registration(first, last, email, password)
    save_into_database(db_entry)

def save_into_database(user):
    database.append(user)
    
def num_of_users(num):
    for i in range(0, num):
        get_user_info()

num_of_users(5)
print(database)


##########

lakers = [
    {"first_name": Lebron, "last_name": James, "email": lebron@lebron.com}
    {"first_name": Kobe, "last_name": Bryant, "email": kobe@kobe.com}
]

#prints all first_name values
for val in lakers:
    print(val["first_name"])

#prints keys
for val in lakers:
    for i in val:
        print(i)
    for val in val.items():
        print(val)

#prints keys and values
for val in lakers:
    print("---------------------------")
    for key, val, in val.items():
        print(key, val)

for val in lakers:
    print("First Name: {}".format(val['first_name']))
    print("Last Name: {}".format(val['last_name']))
    print("Email: {}".format(val['email']))

    print(f"First Name: {val["first_name"]})

lakers[2]['password'] = 'password'
