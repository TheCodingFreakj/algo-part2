import sys


def frog_jump(height, index):
    jump_two = sys.maxsize
    if (index == 0):
        return 0

    # tells how much enerygy is required from index-1 to 0
    jump_one = frog_jump(heights, index-1) + \
        abs(height[index] - height[index-1])

    if (index > 1):
        jump_two = frog_jump(heights, index-2) + \
            abs(height[index] - height[index-2])
        
    return min(jump_one, jump_two)    


def frog_jump_memoization(height, index,dp):
    jump_two = sys.maxsize
    if (index == 0):
        return 0
    
    #initialize a dp with -1
    if(dp[index] != -1):
        return dp[index]

    # tells how much enerygy is required from index-1 to 0
    jump_one = frog_jump(heights, index-1) + \
        abs(height[index] - height[index-1])

    if (index > 1):
        jump_two = frog_jump(heights, index-2) + \
            abs(height[index] - height[index-2])
        
    dp[index] = min(jump_one, jump_two) 
    return dp[index]

def frog_jump_tabulation(height, n):
    jumpTwo = sys.maxsize
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for ind in range(1, n):
        jumpOne = dp[ind-1] + abs(height[ind]-height[ind-1])
        if ind > 1:
            jumpTwo = dp[ind-2] + abs(height[ind]-height[ind-2])
        dp[ind] = min(jumpOne, jumpTwo)
    print(dp[n-1])

if __name__ == "__main__":
    heights = [30, 10, 60, 10, 60, 50]
    print(frog_jump(heights, len(heights)-1))
    dp = [-1] * len(heights)
    print(frog_jump_memoization(heights, len(heights)-1,dp))
    print(frog_jump_tabulation(heights, len(heights)-1))




