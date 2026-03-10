def facIter(n):
    result = 1
    for i in range(1, n+1): #1 eingeschlossen, n+1 ausgeschlossen
        result = result * i
    return result

print(facIter(4))