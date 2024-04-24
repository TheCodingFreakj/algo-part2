def combinationSum(candidates, target):
    def backtrack(candidates, target, path, result,index):
        if target == 0:
            result.append(path)
            return
        if target < 0 or not candidates:
            return
        print(index,candidates[index])
        # Explore two possibilities: include current candidate or exclude it
        backtrack(candidates[index:], target - candidates[index], path + [candidates[index]], result,index+1)
        backtrack(candidates[index:], target, path, result,index)

    result = []
    backtrack(candidates, target, [], result,0)
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))