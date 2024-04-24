# identify the sorted half
# sorted half may or may not contain the miniumum so we have to take the min from the sorted half
# the rotating point or  unsorted part will always have the min element
import sys
def findMin(arr, low, high):
    min_element = sys.maxsize
    while (low <= high):
        mid = (low+high)//2
        #if both left and right half is sorted
        if(arr[low]<=arr[mid] and arr[mid] <= arr[high]):
            min_element = min(min_element, arr[low])
            break
        # identify the sorted half
        if (arr[low] <= arr[mid]):
            # this left part is sorted
            min_element = min(min_element, arr[low])
            # elemniate the sorted part
            low = mid+1
        else:
            # right part is sorted
            min_element = min(min_element, arr[mid])
            high = mid-1

    return min_element


# Driver program to test above functions
if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    N = len(arr)
    print("The minimum element is " +
          str(findMin(arr, 0, N-1)))
