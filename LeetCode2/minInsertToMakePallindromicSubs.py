def min_insertions_to_palindrome(string):
    n = len(string)
    dp = [[0] * n for _ in range(n)]

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

    return dp[0][-1]


# Example usage:
string = "mbadm"
print("Minimum insertions to make '{}' palindrome: {}".format(
    string, min_insertions_to_palindrome(string)))
