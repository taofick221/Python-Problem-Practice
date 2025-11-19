


# Using lambda function inside another function
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(lambda a, b: a - b, 10, 5)
print(result)









