"""
def fibonacci(number):
    list = [1, 1]
    for num in range(2, number, 1):
        list.append(list[-1] + list[-2])
    return(list)
print(fibonacci(12))
"""

"""
def fibonacci(number):
    if number == 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    
    list = fibonacci(number - 1)
    list.append(list[-1] + list[-2])
    return list

print(fibonacci(1000))
"""

"""
def factorial(number):
    if number == 0:
        return 1
    result = factorial(number - 1)
    result *= number
    return result

print(factorial(1000))
"""

"""
def imperfect_harmonic(extent):
    if extent == 1:
        return 1
    result = 1 + (imperfect_harmonic(extent - 1) - 1)
    result += 1/extent
    return result

print(imperfect_harmonic(100))
"""

def gcd_finder(x, y):
    """if x == y:
        return x
    return gcd_finder(max(x, y) - min(x, y), min(x, y))"""
    if y == 0:
        return x
    return gcd_finder(y, (x % y))

print(gcd_finder(48, 18))