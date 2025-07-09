"""______Return maximum occuring character in the input string______"""

def max_occuring_character(s):
    char = max(set(s), key =s.count)
    return char, s.count(char)

input_string = "Hello World"
chr, cnt = max_occuring_character(input_string)
print(f"max occuring character: {chr} which occurs {cnt} times")