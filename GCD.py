def GCD(a, b):
    # Find which is smaller in two numbers
    c = min(a, b)

    # Start check from the minimum number
    # Every time the number will reduced by 1
    for i in range(c, 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i


d = GCD(3, 4)
print(d)