def insertWordMiddle():
    str = "Hello World"
    to_be_inserted = "Programming"
    mid = len(str)//2

    left_half = str[:mid+1]
    right_half = str[mid:]

    str = left_half + to_be_inserted + right_half
    return str


insertWordMiddle()    
