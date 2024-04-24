class Solution:
    def subsetSums(self, arr, n):
        ans = []
        subsets = []

        def subsetSumsHelper(ind, sum):
            # the array is complete

            if (ind == len(arr)):
                ans.append(sum)
                return

            # picking the index
            subsetSumsHelper(ind+1, sum + arr[ind])

            # not picking the index
            subsetSumsHelper(ind+1, sum)

        subsetSumsHelper(0, 0)
        ans.sort()
        return ans


if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()
