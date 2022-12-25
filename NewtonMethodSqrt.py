def sqrt(num, l):
    x = num
    while 1:
        # calculate more precise value of root
        root = 0.5 * (x + (num / x))

        # check for precision
        if abs(root - x) < l:
            break

        # update root
        x = root
    return root


# The lesser the value of l, more time the loop will run
# And more precise will be the ans
print(sqrt(25, 0.00001))   
