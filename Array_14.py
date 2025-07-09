"""______Search for element in an array______"""

from array import *
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

a = array('i',[1,2,3,4,5,6])
target_element = 5
result = linear_search(a, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")