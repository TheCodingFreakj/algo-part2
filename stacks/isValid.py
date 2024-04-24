def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    validParanthesis = []

    
    #char is the key
    #mapping[char] is the value
    for char in s:
        if(char in mapping): # collecting all the closing elements from the mappings
            #check if the stack is empty or not
            if not stack:
                return False
            else:
                top_ele = stack.pop() # grab the top element of the stack
            #check if the correspoinding opening braces with the topele
            if mapping[char] != top_ele:
                return False 
            else:
                return True   
        else:
            stack.append(char) # grabbing all the opening elements in the stacking        
s = "()[]{}"
print(isValid(s))            