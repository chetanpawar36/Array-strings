"""______Find average of all the elements in an array______"""

from array import *
def calculate_avg(arr):
    if len(arr) == 0:
        return 0
    total_sum = sum(arr)
    avg = total_sum // len(arr)
    return avg

a = array('i',[2,2,2,3,3,6])
avg_elmn = calculate_avg(a)
print(f"The average of all the elements of given {a} is: {avg_elmn}")