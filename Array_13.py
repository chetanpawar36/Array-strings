"""______Find all non-repeating elements in an array______"""
 
from array import *
from collections import Counter

def find_non_rep(arr):
    element_count = Counter(arr)
    non_rep = [element for element, count in element_count.items() if count == 1]
    return non_rep

a = array('i', [2,4,3,5,4,6,2])
fnd_nrep = find_non_rep(a)
print(f"The non-repeating elements from given {a} are: {fnd_nrep}")