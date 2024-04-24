def combinationSum2(candidates, target):
    ans = []
    ds = []
    candidates.sort()

    def findCombination(ind, target):
        if target == 0:
            ans.append(ds[:])
            return

        # loop from ind to n -1
        for i in range(len(candidates)):
            # don't pick if candidate[i] == candidate[i+1]
            if (i > ind and candidates[i] == candidates[i - 1]):
                continue
            # come out of the loop if candidate[i]> target
            if (candidates[i] > target):
                break
            # pick otherwise
            ds.append(candidates[i])
            findCombination(i+1, target-candidates[i])
            ds.pop()

    findCombination(0, target)
    return ans


if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(*comb)
