"""______Find the circular rotation of an array by K positions______"""

from array import *
def circular_rot(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

a = array('i',[2,5,4,1])
print(f"The original array:{a}\nThe circular rotation by k positions, so array will be {circular_rot(a, 3)}")