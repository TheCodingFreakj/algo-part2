def all_numbers(num, ds):
    if (num == 0):
        return ds
    first_digit = (num//10)
    second_digit = (num % 10)

    if (first_digit >= 0 and first_digit <= 1000):
        num = first_digit
        ds.append(second_digit)
        all_numbers(num, ds)


def check_common_digit(num1, num2):
    if(num1 == num2):
        return True

    if ((num1 < 0 and num1 > 1000) or (num2 < 0 and num2 > 1000)):
        return False
    else:
        ds = []
        all_numbers(num1, ds)
        all_numbers(num2, ds)
        print(ds)

        if(len(ds) == len(set(ds))):
            return False
        else:
            return True




n, n1 = 35, 45
print(check_common_digit(n, n1))
