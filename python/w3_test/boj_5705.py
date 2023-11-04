from collections import defaultdict
from sys import stdin

stdin = open("input.txt", "r")

# INF = int(1e9)

dp = defaultdict(int)

def fib(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

N = int(stdin.readline())
# while N != 0:
#     memo = {key: 0 for key in range(N)}
#     fibo(N)
#     N = int(stdin.readline())

print(fib(4))