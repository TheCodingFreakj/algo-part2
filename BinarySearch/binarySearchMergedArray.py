# There are two arrays
# we have to find the median of the merged array
# step1
# partition the first array and see what are the number of elements on the left and right side
# partition the second array such that
# if(max(first array before partiton)) <= min(second array after partirtion)
# and
# if(max(second array before partition))<= min (first array after partition)

# the diagonal elements of both the arrays, then evenry element on the left
# of the combined array is greater than every element on the right of the combined array

# partition x + partition y = (x+y +1)/2 x = no of element in array 1 and y = no of element in array2
# maxLeftx <= minRighty and maxLefty <= minRghtx then median is reached
# maxLeftx > minRighty = we are on the too much on the right side of x then we need to
# move to the left side of x other move the binary search to the rght side of x


def Median(A, B):
    length_a = len(A)  # length of smaller array
    length_b = len(B)
    mid_in_merged_array = (length_a + length_b + 1)//2


    #consider the smaller array
    start = 0
    end = length_a
    

    while (start <= end):
        mid_of_small_arr_a = (start+end)//2
        partition_a = mid_of_small_arr_a
        partition_b = mid_in_merged_array - partition_a

        # getting max element of left half in A which is one element left of mid in arraay A
        maxLeftX = A[partition_a-1] if (partition_a > 0) else float('-inf')
        # getting max element of left half in B which is one element left of mid in arraay B
        maxLeftY = A[partition_b-1] if (partition_b > 0) else float('-inf')

        # getting min element of right half of A whch is the mid element in arrayA
        minRightX = A[partition_a] if partition_a < length_a else float('inf')
        # getting min element of right half of B whch is the mid element in arrayB
        minRightY = A[partition_b] if partition_b < length_a else float('inf')

        if(maxLeftX <= minRightY) or (maxLeftY <= minRightX):
            print("found the mid of merged array")
            if ((length_a + length_b) % 2 == 0):
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            return max(maxLeftX, maxLeftY)
        elif(maxLeftX> minRightY):
            print("we are too much on the right side go to more left")
            print("moving the end to left for smaller array A") 
            print("make the end to the one lement before the mid point to search in the left side")
            end = mid_of_small_arr_a -1  
        else:
            print("go to the right side of the array")
            print("make the start to element after the mid element to search in right side ")
            start = mid_of_small_arr_a + 1    


arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

print(Median(arr1, arr2))
