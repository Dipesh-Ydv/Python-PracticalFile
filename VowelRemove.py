def rmVowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ''
    for i in range(len(string)):
        if string[i] not in vowels:
            ans = ans + string[i]
    print(ans)

rmVowel('Dipesh Yadav')