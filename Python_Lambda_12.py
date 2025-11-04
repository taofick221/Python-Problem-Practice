


# Lambda function with no parameters
greet = lambda: "Hello, World!"
print(greet())


# Using lambda function inside another function
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(lambda a, b: a - b, 10, 5)
print(result)


# Lambda function with conditional expression
max_value = lambda a, b: a if a > b else b  
print(max_value(10, 20))
print(max_value(30, 15))



# Using lambda with map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)






