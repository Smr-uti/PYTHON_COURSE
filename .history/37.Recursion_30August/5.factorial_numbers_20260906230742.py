def factorial_numbers(n):
    if n == 1:
        return 1
    return n * factorial_numbers(n-1)

num = 5
print(factorial_numbers(num))