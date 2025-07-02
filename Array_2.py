"""______Reversal of an array______"""

import array
def reversal(arr):
    arr.reverse()
    return arr
a = array.array('i',[2,4,4,6,8])
revs_arr = reversal(a)
print(f"The reversal of given {a} is as: {revs_arr}")