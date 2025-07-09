"""______Calculate frequency of characters in a string______"""

def cal_freq(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_string = "Hello World"
print(f"Character frequency: {cal_freq(input_string)}")