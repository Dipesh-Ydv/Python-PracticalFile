def rmVowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ''
    for i in range(len(string)):
        if string[i] not in vowels:
            ans = ans + string[i]
    print(ans)

str = input('Enter the string: ')
print('String before removing vowels:')
print(str)
print('String after removing vowels:')
rmVowel(str)