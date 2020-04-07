x = "Hello Python"
print(x)
y=42
print(y)

def sum(a,b):
    print("a:", a, "b:", b) # prints the values of a and b
    return a+b # returns the sum of a+b
print(sum(3,5))
print(sum(2,4)+sum(1,5))

count = 0
while count < 5: # notice the colon!
    print("looping - ", count)
    count += 1