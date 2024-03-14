def fibonacci(num):
    if num <= 1:
        return 1
    return num * fibonacci(num - 1)


print(fibonacci(5))
