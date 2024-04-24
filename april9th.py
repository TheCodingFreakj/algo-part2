def calculate_digit_sums(n):
    even_sum = 0
    old_sum = 0

    for single_digit in str(n):

        if (int(single_digit) % 2 == 0):
            even_sum = even_sum+int(single_digit)
        else:
            old_sum = old_sum + int(single_digit)

    return even_sum, old_sum        
    # if (n == 0):
    #     return even_sum, old_sum
    # single_digit = n % 10
    # if (single_digit % 2 == 0):
    #     even_sum = even_sum+single_digit
    # else:
    #     old_sum = old_sum + single_digit

    # return calculate_digit_sums(n//10, even_sum, old_sum)


n = 987654
even_sum = 0
old_sum = 0
print(calculate_digit_sums(n))
