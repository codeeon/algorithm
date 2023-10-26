import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input(): return sys.stdin.readline().strip()





# 입력
N = int(input())
data = list(map(int, input().split()))

for _ in range(N):
    n, m = map(int, input().split())

# txt file 입출력
# "args": ["<", "input.txt", ">", "output.txt" ] --> "args": ["<input.txt", "output.txt" ]


# 출력
print(n)
print(data)