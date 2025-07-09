"""______Find the maximum product subarray in an array______"""

from array import *
def max_prod_subarr(arr):
    max_prod = min_prod = result = arr[0]

    for num in arr[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    
    return result

a = array('i', [2,3,5,-4])
print(f"The maximum product subarray in an array {a} is: {max_prod_subarr(a)}")