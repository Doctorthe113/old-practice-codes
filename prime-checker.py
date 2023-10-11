import timeit

code = """def check(num):
    if (num == 1):
        return "This not a prime number"
    elif (num > 1):
        for i in range(2, num):
            if (num % i == 0):
                return "This is not a prime number"
        return "This is a prime number"


print(check(999999999989))"""

elapsed = timeit.timeit(code, number=10)

print(elapsed*1000)