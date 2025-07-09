"""______Remove spaces from the string______"""

def remv_spaces(s):
    return s.replace(" ", "")

input_string = "Hello World"
print(f"For the string '{input_string}', after removing spaces it becomes: {remv_spaces(input_string)}")