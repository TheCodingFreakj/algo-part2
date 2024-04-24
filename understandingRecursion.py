def factorial(n, ds, recursiveCountForward):

    if n == 0:
        return 1
    else:
        recursiveCountForward = recursiveCountForward+1
        # Recursive call to factorial with modified argument
        recursive_result = n * factorial(n - 1, ds, recursiveCountForward)
        ds.append(recursive_result)
        return recursive_result


# Example usage:
ds = []
recursiveCountForward = 0

result = factorial(4, ds, recursiveCountForward)
print(result)
