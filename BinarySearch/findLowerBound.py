def lowerBound(arr, n, x):
    low = 0
    high = n-1
    lower_bound = n
    while(low <= high):
        mid = (low+high)//2

        if(arr[mid]>=x):
            lower_bound = mid
            high = mid -1 #eleminate the right half 
             #because we need the smallest index which can come in the left side
        else:
            #elimiate the left half
            low = mid+1

    return lower_bound           




#we need to find the smallest index which is greater equal to x

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)