class Solution:
    def combinationSum(self, candidates, target):
        combinationSum = []
        ds = []
        def findCombinations(ind, target):
            #base case where the recursion would stop
            if(ind == len(candidates)): 
                if(target == 0):
                    combinationSum.append(ds[:])
                return     

            #scenario where we pick the current element at index ind     
            if(candidates[ind] <= target):
                #pick that element and put it in data structure
                ds.append(candidates[ind])
                findCombinations(ind, target-candidates[ind])
                #when you backtrack you need to have the ds that is present previously
                ds.pop()


           #scenario where we dont pick the current element at index ind
           #candidate[ind] > target so cannot pick candidate [ind]     
            findCombinations(ind+1, target)    


        findCombinations(0, target)
        return combinationSum

        



if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
  
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()