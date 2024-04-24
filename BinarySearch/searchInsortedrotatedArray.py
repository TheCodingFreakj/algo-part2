# Search an element in sorted and rotated array using
# single pass of Binary Search

# Returns index of key in arr[l..h] if key is present,
# otherwise returns -1
def search(arr, l, h, key):
    while (l <= h):
        mid = (l + h) // 2

        if (key == arr[mid]):
            print(mid)
            return mid

        # check which half is sorted
        if arr[l] <= arr[mid]:
            # left half is sorted
            # search if the target is present in left half
            if (arr[l] <= key and key <= arr[mid]):
                # key lies in the left half
                # eleminate the right half
                h = mid-1
                return search(arr, l, h, key)
            else:
                # eleminate the left by moving the low to mid +1
                l = mid+1
                return search(arr, l, h, key)

        else:
            # right half is sorted

            if (arr[mid] <= key and key <= arr[h]):
                # key lies in the left half of right  side
                l = mid + 1
                return search(arr, l, h, key)
            else:
                h = mid - 1
                return search(arr, l, h, key)
    return -1

# Driver program
if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    key = 3
    i = search(arr, 0, len(arr)-1, key)
    if i != -1:
        print("Index: % d" % i)
    else:
        print("Key not found")

# This code is contributed by Shreyanshi Arun
