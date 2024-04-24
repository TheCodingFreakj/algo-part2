# Search an element in sorted and rotated array using
# single pass of Binary Search

# Returns index of key in arr[l..h] if key is present,
# otherwise returns -1
def searchduplicateRotated(arr, l, h, key):
    pass


# Driver program
if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    key = 3
    i = searchduplicateRotated(arr, 0, len(arr)-1, key)
    if i != -1:
        print("Index: % d" % i)
    else:
        print("Key not found")

# This code is contributed by Shreyanshi Arun
