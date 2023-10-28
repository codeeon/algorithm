
# 3차 시도

import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input(): return sys.stdin.readline().strip()

N = int(sys.stdin.readline())

for i in range(N):
    results = []
    prev_e = []

    def dfs(e):
        if len(e) == 0:
            results.append(prev_e[:])

        for a in e:
            next_e = e[:]
            next_e.remove(a)

            prev_e.append(a)
            dfs(next_e)
            prev_e.pop()

    cases = (sys.stdin.readline())
    case = [i for i in cases if i != '\n']
    print(f'Case # {i+1}:')
    dfs(case)
    
    for result in results:
        print(''.join(result))  





# 2차 시도 - itertools.permutations 사용 - 맞음

# import sys
# from itertools import permutations

# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
# def input(): return sys.stdin.readline().strip()

# N = int(sys.stdin.readline())

# for i in range(N):
#     cases = (sys.stdin.readline())
#     case = [i for i in cases if i != '\n']
    
#     n = len(case)
    
#     results = list(permutations(case, n))

#     print(f'Case # {i+1}:')
#     for result in results:
#         print(''.join(result))





# 1차 시도 - 틀렸다고 나옴

# import sys

# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
# def input(): return sys.stdin.readline().strip()

# N = int(sys.stdin.readline())

# for i in range(N):
#     results = []
#     prev_e = []

#     def dfs(e):
#         if len(e) == 0:
#             results.append(prev_e[:])

#         for a in e:
#             next_e = e[:]
#             next_e.remove(a)

#             prev_e.append(a)
#             dfs(next_e)
#             prev_e.pop()

#     cases = (sys.stdin.readline())
#     case = [i for i in cases if i != '\n']
#     print(f'Case # {i+1}:')
#     dfs(case)
    
#     for j in range(len(results)):
#         answer = ''.join(results[j])
#         print(answer)  