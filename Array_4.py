"""______Count the frequency of each element in an array______"""

from array import *
def count_freq(arr):
    freq = {}
    for element in arr:
        if element not in freq:
            freq[element] = arr.count(element)

    return freq

a = array('i',[2,2,3,4,5,6,4,3,5,6,7])
cnt_freq = count_freq(a)
print(f"From the given {a}, count of frequency of each element is: {cnt_freq}")
