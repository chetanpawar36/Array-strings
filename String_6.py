"""______Remove characters from the string except alphabets______"""

def remv_non_alphabets(s):
    return ''.join(char for char in s if char.isalpha())

input_string = "Hello World! 123"
print(f"Given string '{input_string}', after removing characters from the string except alphabets becomes: {remv_non_alphabets(input_string)}")