# Given two strings,
# find the minimum number of operations
# required to convert one string into the other,
# where the operations include insertion, deletion, or substitution of a character.

def min_operations(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp[][] in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]:  # if the current character match no operation is needed
                # take the diagonal element and put in current
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]




# Example usage:
str1 = "kitten"
str2 = "sitting"
print("Minimum operations required:", min_operations(str1, str2))
