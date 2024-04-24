def find_subsets(nums, target, index, current_subset, subsets):
    nums.sort()
    if index >= len(nums):
        # Base case: reached the end of the array
        if sum(current_subset) == target:
            subsets.append(current_subset.copy())  # Found a subset with sum equal to target
        return

    # Pick the current element
    current_subset.append(nums[index])
    find_subsets(nums, target, index + 1, current_subset, subsets)

    # Non-pick the current element
    current_subset.pop()
    find_subsets(nums, target, index + 1, current_subset, subsets)

# Example usage:
nums = [1,2,3,4]
target = 6
subsets = []
find_subsets(nums, target, 0, [], subsets)
print(subsets)
