"""______Replace each element of the array by its rank in the array______"""

from array import *
def rep_by_rank(arr):
    sorted_uniq = sorted(set(arr))
    rank_map = {value: rank + 1 for rank, value in enumerate(sorted_uniq)}
    
    ranked_array = array('i', [rank_map[element] for element in arr])
    
    return ranked_array

a = array('i',[50,20,30,10])
print(f"The original array is:{a} and thus the ranked one is:{rep_by_rank(a)}")