# Program Statement

# Given two strings text1 and text2,
# return the length of their longest common subsequence.
# If there is no common subsequence, return 0.

# Define state
# 2D matrix to have text1 in row and text2 in column

def longest_common_subsequence(text1, text2):
    text1Length = len(text1) + 1
    text2Length = len(text2) + 1

    dp = [[0] * text2Length for _ in range(text1Length)]
    print(dp)

    for text1Row in range(1,text1Length):
        # print(text1Row,text1[text1Row-1])
        # print("######################################")
        for text2Col in range(1, text2Length):  
            # print(text2Col, text2[text2Col-1])
            if(text1[text1Row-1] == text2[text2Col-1]):
                #we are incrementing the value stored in the diagonally left element by 1
                #dp33 = dp22+1
                dp[text1Row][text2Col] = dp[text1Row-1][text2Col-1] +1
            else:
                #To update ij33 we take the max of the values stored in d23 oe d32
                dp[text1Row][text2Col] = max(dp[text1Row][text2Col-1], dp[text1Row-1][text2Col])

    print(dp[text1Length-1][text2Length-1])
# Example usage:
text1 = "abcde"
text2 = "ace"
print(longest_common_subsequence(text1, text2))  # Output should be 3
