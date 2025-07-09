"""______Check if two strings are anagrams of each other______"""

def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

str1 = "listen"
str2 = "silent"
print(f"Are the two strings anagrams? {are_anagrams(str1, str2)}")