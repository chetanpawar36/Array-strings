"""______Rotate an array by k elements - Block Swap Algorithm______"""

from array import *
def swap(arr, start1, start2, count):
    arr[start1: start1 + count], arr[start2: start2 + count] = arr[start2:start2 + count], arr[start1:start1 + count]

def block_swap_rotate(arr, n, k):
    k = k % n
    if k == 0:
        return
    
    swap(arr, 0, n - k, k)
    swap(arr, k, n - k, n - k)

a = array('i', [1, 2, 3, 4, 5, 6, 7])
print(f"Original array: {list(a)}")
block_swap_rotate(a, len(a), 3)
print(f"After rotating by k elements - Block Swap Algorithm, it becomes: {list(a)}")