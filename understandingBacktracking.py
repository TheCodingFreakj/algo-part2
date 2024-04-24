def understandBacktracking(arr, ds, startIndex, currentSum, target,results):

    if currentSum == target:
        results.append(ds[:])
        #on this condition met the control flows to where it is called from
        return


    #on this condition met the control flows to where it is called from
    if currentSum > target or startIndex >= len(arr):
        return
    ds.append(arr[startIndex])
    #the control flows here after any base condition is met
    understandBacktracking(arr, ds, startIndex+1, currentSum+arr[startIndex], target,results)
    #executes the next statement this is backtracking statement
    ds.pop()


    #after the pop we are just incrementing the index without incrementing the sum
    #this is to try the next element with the previous combination
    understandBacktracking(arr, ds, startIndex+1,currentSum, target,results)

    #will not return results to the main func untill the above recursive call is finished
    return results
    


arr = [3, 34, 4, 12, 5, 2,9]
target = 9
ds = []
startIndex = 0
currentSum = 0
print(understandBacktracking(arr, ds, startIndex, currentSum, target,[]))
