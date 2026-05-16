def quicksort(list):
    if len(list) < 2:
        return list
    
    pivot = list[0]
    min_list = [i for i in list[1:] if i <= pivot]
    max_list = [i for i in list[1:] if i > pivot]
    return quicksort(min_list) + [pivot] + quicksort(max_list)

print(quicksort([3, 2, 5, 1, 4]))