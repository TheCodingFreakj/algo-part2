def longest_palindromic_substring(s):
    n = len(s)
    if n <= 1:
        return s

    # Initialize a table to store results of subproblems
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Initialize variables to store the start and max length of the longest palindrome found
    start = 0
    max_len = 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for substrings of length > 2
    for length in range(3,n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]


    # Example usage:
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"
