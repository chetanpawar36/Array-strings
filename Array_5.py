"""______Rearrange the array in the increasing-decreasing order______"""

import array
def rearrange_increasing_decreasing(arr):
    sorted_list = sorted(arr)
    mid = (len(sorted_list)+1) // 2
    result = []
    result.extend(sorted_list[:mid])
    result.extend(reversed(sorted_list[mid:]))
    return array.array(arr.typecode, result)

a = array.array('i',[1,2,3,4,5,6,7])
rng_inc_dec = rearrange_increasing_decreasing(a)
print(f"The given {list(a)} in increasing-decreasing order is: {list(rng_inc_dec)}")