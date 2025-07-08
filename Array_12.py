"""______Find all repeating elements in an array______"""

from array import *
def find_repeating_elements(arr):
    seen = set()
    repeating = set()

    for element in arr:
        if element in seen:
            repeating.add(element)
        else:
            seen.add(element)
    return list(repeating)

a = array('i',[1,3,5,7,5,2,5,7])
fnd_rep = find_repeating_elements(a)
print(f"The repeating elements from the given {a} is {fnd_rep}")