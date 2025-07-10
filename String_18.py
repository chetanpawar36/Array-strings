"""______Check if two strings match where one string contains wildcard characters______"""

def is_match(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len(s)][len(p)]

string1 = "Hello_World"
pattern1 = "Hello_*"

if is_match(string1, pattern1):
    print(f"The string '{string1}' matches the pattern '{pattern1}'.")
else:
    print(f"The string '{string1}' does not match the pattern '{pattern1}'.")
