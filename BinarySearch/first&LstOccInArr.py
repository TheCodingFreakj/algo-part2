

def first(arr, low, high, x, n):
    firstInd = -1
    while (low <= high):
        mid = (low+high)//2
        if (x == arr[mid]):
            print("getting the first element")
            return mid
        if (arr[low] <= x and x <= arr[mid]):
            print("we are in the left half")
            high = mid - 1
            return first(arr, low, high, x, n)
        else:
            print("we are in the right half")
            low = mid + 1
            return first(arr, low, high, x, n)    


def last(arr, low, high, x, n):
    lastInd = -1
    while (low <= high):
        mid = (low+high)//2
        if (x == arr[mid]):
            print("getting the last element")
            return mid
            
        if (arr[high] >= x and x >= arr[mid]):
            low = mid + 1
            return last(arr, low, high, x, n)
        else:
            high = mid - 1
            return last(arr, low, high, x, n)
    return lastInd       


# Driver program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)

x = 2
print("First Occurrence = ",
      first(arr, 0, n - 1, x, n))
# print("Last Occurrence = ",
#       last(arr, 0, n - 1, x, n))


