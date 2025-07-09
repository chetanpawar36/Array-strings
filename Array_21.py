"""______Sort an array according to the order defined by another array______"""

from array import *
def sort_by_order(arr, order):
    order_map = {value: index for index, value in enumerate(order)}
    sorted_arr = sorted(arr, key=lambda x: order_map.get(x, float('inf')))
    return sorted_arr

a = array('i', [3,5,4,7])
order = [4,5]
print(f"The original array: {a}\nThe array according to the given order: {sort_by_order(a, order)}")