def natural_numbers(n):
    if n < 1:
        return
    print(n)
    natural_numbers(n-1)

natural_numbers(10)    