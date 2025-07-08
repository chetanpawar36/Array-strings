"""______Add an element in an array______"""

from array import *
def add_element(arr):
    arr.append(99)
    return arr

a = array('i',[1,2,3,4,5])
add_elm = add_element(a)
print(f"After adding element 9, the array becomes: {add_elm}")