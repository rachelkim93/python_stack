Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def makeItBig(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
                arr[i] = "big"
    return arr
print(makeItBig([-1, 3, 5, -5]))

Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPositives(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count += 1
    arr[-1] = count
    return arr
print(countPositives([-1, 1, 1, 1]))
    

SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    count = 0
    for i in range(0, len(arr)):
        count = arr[i] + count
    return count
print(sumTotal([1, 2, 3, 4]))

Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    sum = 0.0
    for i in arr:
        sum += i
    print(sum/len(arr))
average([1, 2, 3, 4, 5])


Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    print(len(arr))
length([1, 2, 3, 4])

Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    # if len(arr) = 0:
    #     print False
    value = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[i+1]:
            value = arr[i]
    print(arr[i])
minimum([1, 3, 2, -2])


def minimum(arr):
    for i in arr:
        mini = arr[0]
        if i < mini:
            mini = i
    print mini
minimum([1, 2, 3, -1])


Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    maxi = arr[0]
    for i in arr:
        if maxi < i:
            maxi = i
    print maxi
maximum([7, 4, 3, 9])

UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimateAnalyze(arr):
    max = arr[0]
    min = arr[0]
    sum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        sum = sum + arr[i]
    print max, min, sum/len(arr), sum-arr[0], len(arr)
ultimateAnalyze([1, 2, 3, 4, 5])


ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverseArray(arr):
    for i in range(0, len(arr)/2):
        temp = arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    print arr
reverseArray([1, 2, 3, 4])