def addMinimum(word: str) -> int:
    validString = "abc"
    count = 0
    letterToBeAdded = []
    resultantStr = ''
    print(word)
    for j in range(len(word)):
        if("ab" in word):
            count = count +1
        if("bc" in word):
            count = count +1 

        if("a" in word):
            count = count +2        
        if("b" in word):
            count = count +2 

        if("c" in word):
            count = count +2      

            




    return letterToBeAdded, resultantStr, count


# word = "b"
word = "aaaaab"  # 9
print(addMinimum(word))
