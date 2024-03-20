def add(a, b):
    if isinstance(a,str) or isinstance(b,str):
        result = "bad input"
        print(result)
        return result
    else:
        result = a + b
        print("The result of adding:",result)
        return result


def subtract(a, b):
    if isinstance(a,str) or isinstance(b,str):
        result = "bad input"
        print(result)
        return result
    else:
        result = a - b
        print("The result of subtracting:",result)
        return result


def multiply(a, b):
    if isinstance(a,str) or isinstance(b,str):
        result = "bad input"
        print(result)
        return result
    else:
        result = a * b
        print("The result of multiplying:",result)
        return result


def divide(a, b):
    if isinstance(a,str) or isinstance(b,str):
        result = "bad input"
        print(result)
        return result
    elif a == 0 or b == 0:
        result = "Cannot divide by zero"
        print(result)
        return result
    else:
        result = a / b
        print("The result of dividing:",result)
        return result


add("Hello",3)
subtract("Hello",3)
multiply("Hello",3)
divide(0,3)

