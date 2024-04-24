def sumUniques(arr):
    answer = []

    def getUniques(arr, index, ds):

        right_half = arr[index+1:]
        left_half = arr[:index]

        #handling if there is only one element
        if (len(nums) == 1):
            answer.append(arr[index])
            return

        # handlinng the last index if duplicates
        if index == len(arr)-1:
            #handling if the last element is present in left half
            if(arr[index]  not in left_half):
                ds.append(arr[index])
                ans = 0
                for i in range(len(ds)):
                    ans = ans + ds[i]
                answer.append(ans)
                return
            
        #handling if last element is not duplicate    
        if (index == len(arr)-1):
            ans = 0
            for i in range(len(ds)):
                ans = ans + ds[i]
            answer.append(ans)
            return
       
       #checking if the element at index is present in left or right half for duplicates
        if ((arr[index] in right_half) or (arr[index] in left_half)):
            getUniques(arr, index+1, ds)
        else:
            #checking if the element at index is not present in left or right half for uniques
            if ((arr[index] not in right_half) or (arr[index] not in left_half)):
                ds.append(arr[index])
            getUniques(arr, index+1, ds)

    getUniques(arr, 0, [])
    return answer[0]


if __name__ == "__main__":
    #nums = [1, 2, 3, 2]
    #nums = [1, 2, 3, 4, 5]
    #nums = [10,4,10,9,5]
    nums = [98, 8, 13, 39, 84, 56, 33, 31, 91, 92, 56, 99]
    print(sumUniques(nums))
