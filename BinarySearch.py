def binarySearch(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        # calculate new mid each time
        mid = int(start + (end - start)/2)

        # return mid index if target is found
        if target == lst[mid]:
            return mid
        # search in the left part of list
        # if target is not at mid index
        elif target < lst[mid]:
            end = mid -1
        # search in the right part of list
        # if target is not at mid index
        else:
            start = mid + 1
    
    # return -1 if target is not found
    return -1


lst = [1,2,5,7,12,22]
target = 12

ans = binarySearch(lst, target)

if ans != -1:
    print('Target element found on index number :', ans)
else:
    print('Target element is not present in the list:(')   
    