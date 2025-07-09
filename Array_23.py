"""______Sort the elements of an array by frequency______"""

from array import *
from collections import Counter
def sort_by_freq(arr):
    freq = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    
    return sorted_arr

a = array('i',[2,3,1,5,4,7,2,3,4,5])
print(f"Original array: {a}\nSorting elements by frequency are:{sort_by_freq(a)}")