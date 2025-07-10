"""______Count common sub-sequence in two strings______"""

def count_common_subsequences(s1: str, s2: str) -> int:
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]

string1 = "abc"
string2 = "abdc"
count = count_common_subsequences(string1, string2)
print(f"The number of common subsequences between '{string1}' and '{string2}' is: {count}")
