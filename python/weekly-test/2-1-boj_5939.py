import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input(): return sys.stdin.readline().strip()

lst = []

N = int(sys.stdin.readline())

for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    lst.append(nums)

lst.sort()

for i in range(len(lst)):
    print(lst[i][0], lst[i][1], lst[i][2])