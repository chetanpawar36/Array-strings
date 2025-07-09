"""______Check if a given string is palindrome or not______"""

def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"Given string '{input_string}' is a palindrome")
else:
    print(f"Given string '{input_string}' is not a palindrome")