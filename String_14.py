"""______Print all the duplicates in the input string______"""

def prt_duplicates(s):
    return set(char for char in s if s.count(char)>1)

input_string = "hello world"
print(f"Duplicate characters: {prt_duplicates(input_string)}")