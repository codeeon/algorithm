import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input(): return sys.stdin.readline().strip()





from sys import stdin
stdin.readline().strip()





from sys import stdin
import heapq


N = int(stdin.readline())

for i in range(N):
    data = int(stdin.readline())




# 입력
N = int(input())
data = list(map(int, input().split()))

for _ in range(N):
    n, m = map(int, input().split())

# txt file 입출력
# "args": ["<", "input.txt", ">", "output.txt" ] --> "args": ["<input.txt", "output.txt" ]




import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input(): return sys.stdin.readline().strip()

N = int(sys.stdin.readline())

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())





# 출력
print(n)
print(data)






import sys

with open('input.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())
    tri = []
    for _ in range(N):
        tri.append(list(map(int, input().split())))

    memo = [[INF] * (i + 1) for i in range(N)]
    memo[0][0] = tri[0][0]


    def dp(r, c):
        if not (0 <= r < N and 0 <= c < len(tri[r])):
            return 0
        
        if memo[r][c] != INF:
            return memo[r][c]
        
        memo[r][c] = tri[r][c] + max(dp(r - 1, c - 1), dp(r - 1, c))
        return memo[r][c]


    for col in range(N):
        dp(N - 1, col)

    print(max(memo[N - 1]))