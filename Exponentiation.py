import math as M

def expo(base, power):

    return base ** power

base = int(input('Enter the number :'))
power = int(input('Enter the power :'))
print(base, 'power', power, 'is equal to : ', expo(base, power))

# Finding using math modulo
print(base, 'power', power, 'is equal to : ', M.pow(base, power))