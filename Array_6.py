"""______Calculate the sum of the elements in an array______"""

from array import *
def calculate_sum(arr):
    return sum(arr)

a = array('i',[1,1,2,2,3,6])
cls_sum = calculate_sum(a)
print(f"The sum of the given {a} is: {cls_sum}")