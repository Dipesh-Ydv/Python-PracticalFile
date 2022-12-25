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

def nPrimeNo(num):
    # Check for each number is it prime or not
    for i in range(1,num+1):
        if isPrime(i) == True:
            print(i)


num = int(input('Enter a number to get prime till that : '))
print('Prime no till', num, 'are :')
nPrimeNo(num)
