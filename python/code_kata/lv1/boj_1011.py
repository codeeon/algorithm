import sys, math

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())

    d = y - x

    answer = math.ceil(2 * math.sqrt(d)) - 1
    print(answer)