# https://chat.openai.com/share/6ea75a1a-8c4e-4746-9135-2424b70b3ac1

#implement memoization
def subset_sum_recursive(nums, target, index, current_sum, result, ds,memo):
    # [3, 34, 4, 12, 5, 2]
    if (current_sum == target):
        result.append(ds[:])
        return
    if current_sum > target or index >= len(nums):
        return

    # include the current element
    ds.append(nums[index])
    subset_sum_recursive(nums, target, index+1,current_sum + nums[index], result, ds,memo)
    ds.pop()

    # exclude the current element
    subset_sum_recursive(nums, target, index+1, current_sum, result, ds,memo)




def subset_sum(nums, target):
    result = []
    ds = []
    memo = {}
    subset_sum_recursive(nums, target, 0, 0, result, ds,memo)
    return result


# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target))  # Output: True
