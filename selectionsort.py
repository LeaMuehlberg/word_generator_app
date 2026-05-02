def findSmallest(arr):
    smallest = arr[0]
    smallest_in = 0

    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_in = i
    return smallest_in

def aufSelectionSort(arr):
    newArr = []
    for i in range (len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(aufSelectionSort([4, 78, 34, 9]))

def findBiggest(arr):
    biggest = arr[0]
    biggest_in = 0

    for i in range (1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_in = i
    return biggest_in

def abSelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr

print(abSelectionSort([4, 78, 34, 9]))