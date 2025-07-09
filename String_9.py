"""______Sum of the numbers in a string______"""

import re
def sum_of_numbers(s):
    numbers = re.findall(r'\d+', s)
    return sum(int(num) for num in numbers)

input_string = "The 2 cats have 3 lives each, totaling 6 lives"
print(f"Sum of the numbers from the given string '{input_string}' is: {sum_of_numbers(input_string)}")