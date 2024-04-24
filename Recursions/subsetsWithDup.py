from typing import List




class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        ds = []
        nums.sort()
        def findSubsets(ind):
            ans.append(ds[:])
            #run the loop from ind to n-1
            for i in range(ind,len(nums)):
                #leave the duplicates
                if(i != ind and nums[i] == nums [i-1]):
                    continue
                #pick the ind
                ds.append(nums[i])
                findSubsets(i+1)
                ds.pop()
        findSubsets(0)
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print(*ans)