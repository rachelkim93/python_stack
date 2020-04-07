Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].


def countDown(num):
    newArr = []
    for i in range(num, 0, -1):
        newArr.append(i)
    print(newArr)
countDown(5)

Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printAndReturn(arr):
    print(arr[0])
    return arr[1]
printAndReturn([5, 3])

First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlusLength(arr):
    print(arr[0] + len(arr))
firstPlusLength([5, 1, 2])

Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False

def greaterThanSecond(arr):
    newArr = []
    if len(arr) == 1:
        return False
    for i in range(0, len(arr)):
        if arr[i] > arr[1]:
            newArr.append(arr[i])
    print(newArr)
    print(len(newArr))
greaterThanSecond([5, 2, 3, 1, 4])

This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(x, y):
    newArr = []
    for i in range(0, x):
        newArr.append(y)
    print newArr

lengthAndValue(5, 2)