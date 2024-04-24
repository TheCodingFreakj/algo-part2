def is_looping_number(n):
    if (n < 10):
        return True
    first_digit = ((n//10) ** 2)
    second_digit = ((n % 10) ** 2)
    if (first_digit + second_digit == 1):
        return True
    if (first_digit + second_digit != 1 and second_digit == 0):
        return False

    return is_looping_number(first_digit + second_digit)


n = 4
squaring_num = 0
print(is_looping_number(n))
