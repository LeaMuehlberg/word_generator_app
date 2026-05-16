def it_sum(arr):
    total = 0
    for elem in arr:
        total += elem
    return total

print(it_sum([2, 4, 6]))

def sum(arr):
    if arr == []: # bzw len(arr) == 0
        return 0
    return arr[0] + sum(arr[1:])

print(sum([2, 4, 6]))