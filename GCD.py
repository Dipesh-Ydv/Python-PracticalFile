def GCD(a, b):
    # Find which is smaller in two numbers
    c = min(a, b)

    # Start check from the minimum number
    # Every time the number will reduced by 1
    for i in range(c, 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
ans = GCD(num1, num2)
print('GCD of', num1, 'and', num2 , 'is:' ,ans)