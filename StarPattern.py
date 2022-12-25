def pattern(num):
    # It will handle number of rows
    for i in range(num):
        # It will handle number of cols
        for j in range(i+1):
            print('*', end="")
        # It will end line after each row
        print('\r')

pattern(8)