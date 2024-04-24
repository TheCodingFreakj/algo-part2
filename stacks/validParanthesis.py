def longestValidParentheses(s: str, index) -> int:
    valids = ''
    validOpeners = ''

    for i in range(len(s)):
        if (s[i] == "("):
            validOpeners = validOpeners + "("
        if (s[i] == ")"):
            valids = valids + ")"

    i = 0
    j = len(validOpeners) -1  
    maxLen = 0
    while(i<len(validOpeners)-1 or j > 0) :
            print(validOpeners, valids)
            print(j,i)
            if j < 0:
                return maxLen
            if i > len(valids):
                return maxLen
            if (i <= len(valids) and validOpeners[j] == "(" and valids[i] == ")"):
                maxLen = maxLen+2
                print( maxLen)
            i = i+1
            j= j-1
    return maxLen         




# s = "(()"  # 2
# s = ")()())"  # 4
s = "()(()"
# s = "()(())" #6
print(longestValidParentheses(s, 0))
