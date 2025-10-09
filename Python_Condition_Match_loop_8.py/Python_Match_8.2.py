# Match case
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(404))


# Match with multiple patterns
def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Client error"
        case 500 | 501 | 502 | 503:
            return "Server error"
        case _:
            return "Unknown error"
print(http_error(500))




# Match with capture pattern
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _ as unknown_status:
            return f"Unknown error: {unknown_status}"
print(http_error(501))



# Match with class pattern
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case Point(0, 0):
            return "Origin"
        case Point(x, 0):
            return f"X={x}, Y=0"
        case Point(0, y):
            return f"X=0, Y={y}"
        case Point(x, y):
            return f"X={x}, Y={y}"
        case _:
            return "Not a point"
print(where_is(Point(0, 0)))
print(where_is(Point(3, 0)))
print(where_is(Point(0, 4)))
print(where_is(Point(5, 6)))



# Match with sequence pattern
def process_list(lst):
    match lst:
        case []:
            return "Empty list"
        case [x]:
            return f"Single element: {x}"
        case [x, y]:
            return f"Two elements: {x}, {y}"
        case [x, y, *rest]:
            return f"First two: {x}, {y}, rest: {rest}"
        case _:
            return "Not a list" 
print(process_list([]))
print(process_list([1]))
print(process_list([1, 2]))
print(process_list([1, 2, 3, 4]))


