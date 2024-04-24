def singleNonDuplicate(arr):
    low = 0
    high = len(arr)-1

    while (low <= high):
        mid = (low+high)//2
        # condition that give which is the single ele
        if ((arr[mid] != arr[mid-1] and arr[mid-1] == arr[low]) and (arr[mid] != arr[mid+1] and arr[mid+1] == arr[high])):
            return arr[mid]
        # handling the high edge case
        if (arr[high] != arr[high-1]):
            return arr[high]
        # handling the low edge case
        if (arr[low] != arr[low+1]):
            return arr[low]
        # decide which part to eliminate
        if (arr[mid] == arr[mid-1]):
            low = mid+1
        if (arr[mid] == arr[mid+1]):
            high = mid-1


# arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
arr = [1,1,2,3,3,4,4]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)
