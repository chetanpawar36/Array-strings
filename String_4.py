"""______Remove all vowels from the string______"""

def remov_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

input_string = "Hello World"
print(f"For the string '{input_string}', after removing vowels it becomes: {remov_vowels(input_string)}")