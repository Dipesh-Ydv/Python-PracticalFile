def bubbleSort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(1,length-i):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp

                # It can also be used for swapping
                # Easy way of swapping
                # (list[j],list[j-1]) = (list[j-1],list[j])   
    return lst

    
lst = []
for _ in range(int(input("Enter length: "))):
    lst.append(int(input("Enter num: ")))
print('List before sorting :', lst)

bubbleSort(lst)
print('List after sorting :', lst)