"""______Count number of vowels, consonants, spaces in a string______"""

def count_char(s):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in s if char in vowels)
    num_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    num_spaces = s.count(' ')
    return num_vowels, num_consonants, num_spaces 

input_string = "Hello World"
vowels, consonants, spaces = count_char(input_string)
print(f"Given string '{input_string}' contains - vowels: {vowels}, consonants: {consonants}, spaces: {spaces}")