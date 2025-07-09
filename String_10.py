"""______Capitalize first and last character of each word______"""

def capitalize_first_and_last(s):
    return ' '.join(word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in s.split())

input_string = "hello world"
print(f'Capitalized string: "{capitalize_first_and_last(input_string)}"')
