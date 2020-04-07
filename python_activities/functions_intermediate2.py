x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print(x)

How would you change the last_name of the first student from 'Jordan' to "Bryant"?

students[0]['last_name'] = "Bryant"
print(student)

For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

For z, how would you change the value 20 to 30?

z[0]['y'] = 30
print(z)



def iterateDictionary():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    for val in students:
        for key, val, in val.items():
            print(key, val)
iterateDictionary()



def iterateDictionary2():
    locations = ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank']
    instructors = ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'mihn', 'Devon']
    count1 = 0
    count2 = 0
    for i in range(len(locations)):
        print(locations[i])
        count1=count1+1
        
    print(count1, ' Locations')

    for j in range(len(instructors)):
        print(instructors[j])
        count2 = count2+1

    print(count2, ' Instructors')
iterateDictionary2()



dojo = {
    'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterateDictionary3(dict):
    for key in dict:
        print(len(dict[key]))
        print(key)
    for i in dict[key]:
        print(i)

iterateDictionary3(dojo)
