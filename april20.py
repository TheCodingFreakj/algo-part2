def reverseString(s):
    stringList = list(s)
    temp = None
    left = 0
    right = len(stringList)-1
    while (left <= right):
        temp = stringList[left]
        stringList[left] = stringList[right]
        stringList[right]= temp

        left = left + 1
        right = right - 1

    return ''.join(stringList)


s = "Hello World!"
reverseString(s)
