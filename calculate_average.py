# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.
numbers = [1,2,3,4,5,6]
def find_average(numbers):
    if sum(numbers) == 0 :
        result = 0
    else:
        result = sum(numbers) / len(numbers)
    return result
find_average(numbers)