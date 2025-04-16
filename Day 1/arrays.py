def sortedSquaredArray(array):
    squared = list(map(lambda a: a*a,array))
    return squared 



def monotonicArray(array):
    count = 0
    for i in range(1,len(array)):
        if array[i-1] <= array[i]:
            count += 1
    return count == 0 or count == len(array)-1

def josephus(n,k):
    winner = 0
    for i in range(2, n+1):
        winner = (winner + k) % i
    return winner + 1


print(sortedSquaredArray([1,2,3,4,5,6,7,8,9]))


print(monotonicArray([1,2,3,4,5,6,7,8,9]))
print(monotonicArray([9,8,7,10,5,4,3,2,1]))
