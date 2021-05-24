def fib1(n):    # write Fibonacci series up to n and output as string
    a, b = 0, 1
    result = ''
    while a < n:
        result += str(a) + ' '
        a, b = b, a+b
    return result


def fib2(n):   # write Fibonacci series up to n and output as list
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
