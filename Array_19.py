"""______Find the equilibrium index of an array______"""

from array import *
def fnd_equ_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, value in enumerate(arr):
        if left_sum == total_sum - value:
            return i
        left_sum += value


a = array('i',[2,7,3,1])
    
if fnd_equ_index(a) != -1:
    print(f"Equilibrium index is: {fnd_equ_index(a)}")
else:
    print("No equilibrium index found.")