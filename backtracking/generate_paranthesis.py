def generateParenthesis(n):
    result = []

    def backtracking(pattern='', left=0, right=0):
        print(pattern, len(pattern))
        if(len(pattern) == 2*n):
            result.append(pattern)
            return

        # check until opening braces are less n
        if (left < n):
            backtracking(pattern + '(', left+1, right)
        if (right < left):
            backtracking(pattern + ')', left, right+1)
    backtracking()
    return result


n = 3
generateParenthesis(n)

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# https://leetcode.com/problems/valid-parentheses/description/
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/
