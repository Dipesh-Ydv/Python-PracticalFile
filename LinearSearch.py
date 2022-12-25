def linearSearch(lst, target):

    for i in range(len(lst)):

        # check for each element in the list
        if (lst[i] == target):

            # return the index if target is found
            return i

    # return -1 if target is not found
    return -1       

lst = [1,2,3,4,5,6]
target = 4

ans = linearSearch(lst, target)

if ans != -1:
    print('Target element found on index number :', ans)
else:
    print('Target element is not present in the list:(')   
    