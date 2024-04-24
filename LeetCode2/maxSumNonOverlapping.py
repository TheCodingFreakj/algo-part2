def max_sum_of_three_subarrays(nums, k, count):
    memo = {}

    # find the max sum at each index and these indexes are k place aways from each other

    # this func returns the count number of starting_index

    def getting_ending_index(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        max_sum_ = 0
        max_idx_ = -1

        for j in range(i, min(i+k, len(nums))):
            current_sum_ = sum(nums[i:j+1])
            if (current_sum_ > max_sum_):
                max_sum_ = current_sum_
                max_idx_ = j

        memo[i] = max_idx_
        return max_idx_

    def findMaxSum(start_index, count, k):
        # will start calculating the maxsum from index0
        if (count == 0):
            return 0, []

        if (start_index >= len(nums)):
            return 0, []

        max_sum = 0
        optimal_indices = []
        for i in range(start_index, len(nums)):
            ending_index = getting_ending_index(i)
            if (start_index == -1):
                break

            # gets the current sum from current element i to ending_index

            current_sum = sum(nums[i:ending_index+1]) + \
                findMaxSum(ending_index + k, count-1, k)[0]

            # logic to give the max_sum
            if (current_sum > max_sum):
                max_sum = current_sum

                optimal_indices = [i] + \
                    findMaxSum(ending_index + k, count-1, k)[1]

            # decide where to start next
            # we have to skip k element to get the next start index
            i = ending_index + k-1

        return max_sum, optimal_indices

    return findMaxSum(0, count, k)[1]


# Example usage:
nums = [1,2,1,2,6,7,5,1]
k = 2
count = 3  # we have to get three non over lapping arrays
# non overlappng means the next subarray should be k distance away from the start index
print(max_sum_of_three_subarrays(nums, k, count))
