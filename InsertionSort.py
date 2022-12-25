def insertionSort(lst):
    
    for i in range(1, len(lst)):
        temp = lst[i]

        j = i-1
        while j >=0 and temp < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = temp


lst = [5,89,23,44,-33,1,0,-1]
print('List before sorting :', lst)

insertionSort(lst)
print('List after sorting :', lst)