# This function will find the index which has the max element
def getMaxIndex(lst, s, e):
    max = s
    for i in range(s,e+1):
        if lst[max] < lst[i]:
            max = i
    return max

def selectionSort(lst):
    for i in range(len(lst)):
        # Last index will change each time
        # Because list will start sorting from last index
        last = len(lst) - i - 1

        # Find the element with max element in remaining list
        maxIndex = getMaxIndex(lst, 0, last)

        # Swap the element with max index with the last index
        (lst[last], lst[maxIndex]) = (lst[maxIndex], lst[last])


lst = [5,4,3,2,1,0,-1]
print('List before sorting :', lst)

selectionSort(lst)
print('List after sorting :', lst)