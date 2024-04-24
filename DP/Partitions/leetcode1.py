# Given an integer array nums and an integer k,
# return true if it is possible to divide this array into k
# non-empty subsets whose sums are all equal.

def canPartitionKSubsets(nums, k):
    total_sum = sum(nums)

    if len(nums) < k:
        return False
    if total_sum % k != 0:
        return False

    sum_each_part = total_sum//k
 

    # declare the dp array

    dp = [[False] * (sum_each_part + 1) for _ in range(len(nums))]

    # Initialize the base case: An empty subset can always achieve a sum of 0.
    for i in range(len(nums)):
        dp[i][0] = True

    # initialize the first element
    if (nums[0] <= sum_each_part):
        dp[0][nums[0]] = True

    for ind in range(1, len(nums)):
        for target in range(1, sum_each_part+1):

            # consider the current element
            taken = False
            if (nums[ind] <= target):
                taken = dp[ind-1][target-nums[ind]]

            # dont consider the current element
            ntaken = dp[ind-1][target]


            dp[ind][target] = ntaken or taken
    return dp[len(nums) - 1][sum_each_part]


# nums = [1,2,3,4]
# k = 3
# nums = [4, 3, 2, 3, 5, 2, 1]
# k = 4
nums = [2, 2, 2, 2, 3, 4, 5]
k = 4
print(canPartitionKSubsets(nums, k))
