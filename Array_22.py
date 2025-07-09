"""_____Find all symmetric pairs in an array_____"""

from array import *
def find_symmetric_pairs(arr):
    seen = {}
    symmetric_pairs = []

    for num in arr:
        if -num in seen:
            symmetric_pairs.append((num, -num))
        seen[num] = True
    return symmetric_pairs

a = array('i',[1, -1, 2, 3, -2, 4, -3, 5])
print(f"Original array: {a}\nThe symmetric pairs are: {find_symmetric_pairs(a)}")