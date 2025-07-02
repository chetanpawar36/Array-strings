"""______Find the second smallest and second largest element in an array______"""

from array import *
def scnd_smallest_scnd_largest(arr):
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None, None
    unique_arr.sort()

    scnd_smallest = unique_arr[1]
    scnd_largest = unique_arr[-2]

    return scnd_smallest, scnd_largest

a = array('i',[2,5,6,9,4])
scnd_smallest, scnd_largest = scnd_smallest_scnd_largest(a)
print(f"From the given array {a}, the second smallest element is {scnd_smallest} and the second largest element is {scnd_largest}")
