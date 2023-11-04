# 백준 1932. 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys





# <input>
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# import sys

# with open('input.txt') as f:
#     sys.stdin = f
#     input = sys.stdin.readline

#     INF = int(1e9)

#     N = int(input())
#     tri = []
#     for _ in range(N):
#         tri.append(list(map(int, input().split())))

#     memo = [[INF] * (i + 1) for i in range(N)]
#     memo[0][0] = tri[0][0]


#     def dp(r, c):
#         if not (0 <= r < N and 0 <= c < len(tri[r])):
#             return 0
        
#         if memo[r][c] != INF:
#             return memo[r][c]
        
#         memo[r][c] = tri[r][c] + max(dp(r - 1, c - 1), dp(r - 1, c))
#         return memo[r][c]


#     for col in range(N):
#         dp(N - 1, col)

#     print(max(memo[N - 1]))