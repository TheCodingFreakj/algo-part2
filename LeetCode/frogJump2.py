import sys

# Recursive function to calculate the minimum cost to reach the end
# from a given index with at most 'k' jumps.







# Helper function to find the minimum jumps required to reach the end
def jump(nums, idx, end, memo):
    # We reached the end. No jumps to make further
    if idx == end:
        return 0
 
    if memo[idx] != -1:
        return memo[idx]
 
    min_jumps = float("inf")
    print(nums[idx])
    # We will try to make all possible jumps from the current index
    # and select the minimum of those.
    # It does not matter if we try from 1 to nums[idx] or from nums[idx] to 1.
    for j in range(len(nums[idx]), 0, -1):
        
        # If we make this jump 'j' distance away from idx,
        # do we overshoot?
        # If we land within the nums, we will test further.
        if idx + j <= end:
            # Make a jump to idx + j index and explore further,
            # then update min_jumps with the minimum jumps
            # we made to reach the end while trying all possible
            # nums[idx] jumps from the current index.
            min_jumps = min(min_jumps, 1 + jump(nums, idx + j, end, memo))
 
    memo[idx] = min_jumps
    return memo[idx]
 
 
def min_jumps(nums):
    """Memoization"""
 
    memo = [-1 for i in range(len(nums))]
    jump(nums, 0, len(nums) - 1, memo)
    return memo[0]


if __name__ == "__main__":
    stones = [0, 2, 5, 6, 7]
    n = len(stones)
    dp = [-1] * n
    print(min_jumps(stones))
    # print(solve(n, stones, 3))
