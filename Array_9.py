"""______Find the median of the given array______"""

import array
def calculate_median(arr):
    if len(arr) == 0:
        return None
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        median = sorted_arr[n//2]
    else:
        mid1 = sorted_arr[n//2-1]
        mid2 = sorted_arr[n//2]
        median = (mid1 + mid2) // 2
        return median

a = array.array('i',[1,2,3,4,5,6,7,8])
med = calculate_median(a)
print(f"The median of the given {a} is: {med}")