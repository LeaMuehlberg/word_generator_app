def it_getBiggest(list):
    biggest = list[0]
    for elem in list:
        if elem > biggest:
            biggest = elem
    return biggest

print(it_getBiggest([3, 1, 45, 23]))

def getBiggest(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    temp_max = getBiggest(list[1:])
    return list[0] if list[0] > temp_max else temp_max

print(getBiggest([3 , 1, 45, 23]))