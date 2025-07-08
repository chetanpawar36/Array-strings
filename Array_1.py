"""______Find the smallest and largest number in an array______"""

import array
def find_smallest_no(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

def find_largest_no(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

a = array.array('i',[1,2,3,4,5])
smallest_number = find_smallest_no(a)
largest_number = find_largest_no(a)
print(f"The smallest number in the given array {a} is: {smallest_number}\nThe largest number in the given array {a} is: {largest_number}")