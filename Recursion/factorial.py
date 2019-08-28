def factorial(n):
    if n == 0:  # base case
        return 1
    elif n > 0:  # recursive case
        return factorial(n - 1) * n


print(factorial(4))
