"""______Check if an array is a subset of another array or not______"""
 
from array import *
def is_subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set2.issubset(set1)

a1 = array('i',[1,2,3,4,5])
a2 = array('i',[2,3,4])

if is_subset(a1, a2):
    print(f"Array {a1} is a subset of Array {a2}.")
else:
    print(f"Array {a1} is not a subset of Array {a2}.")