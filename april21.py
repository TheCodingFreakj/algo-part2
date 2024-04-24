def analyze_string(input_string):
    counts = {"letters": 0, "spaces": 0, "nums": 0, "others": 0}
    for strs in input_string:
        if (strs.isalpha()):
            counts["letters"] = counts["letters"]+1
        elif (strs.isspace()):
            counts["spaces"] = counts["spaces"] + 1
        elif (strs.isdigit()):
            counts["nums"] = counts["nums"] + 1
        else:
            counts["others"] = counts["others"]+1
    
    Values = ''
    for val in [str(v) for k,v in counts.items()]:
        Values = Values + (val) + " "
    return Values

# letters, spaces, numbers, and special characters
input_string = "Hello World! 123"
print(analyze_string(input_string))
