import sys


def min_jumps(nums, index,dp):
    mJumps = sys.maxsize
    #reaching the end of the array, return 0 as there are no more jumps
    if (index >= len(nums)-1):
        return 0
    #if there exists a value for index in dp then return that value
    #this is already been calculated
    if(dp[index] != -1):
        return dp[index]

    #run the loop from index+1 to last index
    last_index = index+nums[index]+1
    for i in range(index+1, last_index):
        #store the min of the mJumps in the variable
        mJumps = min(mJumps, 1+(min_jumps(nums, i,dp)))
    #store the mJumps in the memoized array    
    dp[index] = mJumps 
    #return min of mJumps   
    return mJumps


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    #declaring the array to keep overlapping solutions
    dp = [-1] * len(nums)
    print(min_jumps(nums, 0,dp))
