# Given a non-empty array containing only positive integers,
#  determine whether the array can be partitioned 
# into two subsets such that the sum of elements in both subsets is equal.



def canPartition(nums):
    total_sum = sum(nums)



    target = total_sum//2
    for num in range(len(nums)):
        print("############################################")
        print(target, nums[num])
        print("############################################")
        for j in range(target, nums[num] - 1, -1):
                print(j)
# Example usage:
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True