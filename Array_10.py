"""______Remove duplicates from an sorted array and Remove duplicates from an unsorted array______"""

from array import*
a = array('i',[2,3,2,4,5,6,3,4])
ch = 0
while ch < 2:
    ch = int(input("Please enter 1 for sorted array and 2 for unsorted array: "))
    if ch == 1:
        def remv_dup(arr):
            return list(dict.fromkeys(arr))
        print(f"Original array is: {a}\nAfter removing duplicates(sorted array), it becomes:{remv_dup(a)}")

    elif ch == 2:
        def remvv_dup(arr):
            seen = set()
            uniq_arr = []
            for item in arr:
                if item not in seen:
                    seen.add(item)
                    uniq_arr.append(item)
            return uniq_arr
        print(f"Original array is: {a}\nAfter removing duplicates(unsorted array), it becomes:{remvv_dup(a)}")
    else:
        break