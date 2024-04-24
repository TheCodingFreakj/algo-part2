def max_subarray(nums):
    n = len(nums)
    left = 0
    max_sum = nums[0]

    while (left < n):
        right = left
        while (right < n):
            current_sum = sum(nums[left:right+1])
            if (current_sum > max_sum):
                max_sum = max(current_sum, max_sum)
            right = right+1
        left = left+1

    return max_sum

def maxSubArray(nums):
    max_current = max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)

    return max_global


# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum:", maxSubArray(nums))
