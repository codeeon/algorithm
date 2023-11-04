from sys import stdin

stdin = open("input.txt", "r")

def binary_search(target, start, end):

    while start <= end:
        mid = (start + end) // 2
        
        if mid == target:
            print(mid)
            return
            # result.append(mid)
            # return print(' '.join(map(str, result)))
        elif mid < target:
            print(mid, end=' ')
            # result.append(mid)
            start = mid + 1
        else:
            print(mid, end=' ')
            # result.append(mid)
            end = mid - 1

    return

N = int(stdin.readline())
while N != 0:
    # result = []
    mid = 0
    binary_search(N, 1, 50)
    N = int(stdin.readline())












from sys import stdin

stdin = open("input.txt", "r")

def binary_search(target, start, end):

    while start <= end:
        mid = (start + end) // 2
        
        if mid == target:
            result.append(mid)
            return print(' '.join(map(str, result)))
        elif mid < target:
            result.append(mid)
            start = mid + 1
        else:
            result.append(mid)
            end = mid - 1

    return

N = int(stdin.readline())
while N != 0:
    result = []
    mid = 0
    binary_search(N, 1, 50)
    N = int(stdin.readline())