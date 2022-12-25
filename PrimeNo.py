def isPrime(num):
    flag = True
    if num > 1:
        for i in range(2,(num//2)+1):
            if (num % i) == 0:
                flag = False           
                return flag
            else :
                flag = True
    return flag


num = int(input("Enter a number : "))

if (isPrime(num)):
    print(num , ('is a Prime Number'))
else:
    print(num , 'is not a Prime Number')
