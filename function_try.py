# функція
def print_rectangle_info (a, b):
    perimetr = 2 * a + 2 * b
    squrev = a * b

    print("Retangle", a, "x", b )
    print("perimeter is", perimetr)
    print("Square is", squrev)
    print("----------------------------")

# визов функції
print_rectangle_info(5,8)

def get_result (x, y, c):
    result = x * c / y
    return print(result)

get_result(100,25,46)

def get_result2 (a, b, d):
    result = a * b / d
    return result

print(get_result2(156,234,88))