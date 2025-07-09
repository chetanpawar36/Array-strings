"""______Find non-repeating charcters of a string______"""

def non_rept(s):
    return [char for char in s if s.count(char) == 1]

input_string = "hello world"
print(f"Non-repeating characters: {non_rept(input_string)}")