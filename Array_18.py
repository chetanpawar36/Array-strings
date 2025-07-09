"""______Rotate the elements of an array(left and right)______"""


from array import *
def rot_left(arr, d_L):
    n = len(arr)
    d_L = d_L % n
    return arr[d_L:] + arr[:d_L]
def rot_right(arr, d_R):
    n = len(arr)
    d_R = d_R % n
    return arr[-d_R:] + arr[:-d_R]

a  = array('i',[2,3,1,5])
print(f"The original array is:{a}\nThe array after left rotation is:{rot_left(a, 2)}\nThe array after right rotation is:{rot_right(a, 3)}")