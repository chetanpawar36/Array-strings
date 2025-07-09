"""______Remove all duplicates from the input string______"""

def remv_dup(s):
    seen = set()
    return ''.join(char for char in s if not (char in seen or seen.add(char)))

input_string = "hello world"
print(f"String after removing duplicates is: {remv_dup(input_string)}")