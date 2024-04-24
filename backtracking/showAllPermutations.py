def permute(nums):
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])  # Make a copy of the current permutation
        else:
            for i in range(start, len(nums)):
                # Swap elements to generate different permutations
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)
                # Undo the swap for backtracking
                nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result

# Example usage:
nums = [1, 2, 3]
print(permute(nums))

#need more clarity