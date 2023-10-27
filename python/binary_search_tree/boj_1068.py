# https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-1068-%ED%8A%B8%EB%A6%AC-Python


import sys
from collections import deque

# 노드 개수
N = int(sys.stdin.readline().rstrip())
# 리스트
a = list(map(int, sys.stdin.readline().rstrip().split()))
# 삭제할 노드 번호
dlt = int(sys.stdin.readline().rstrip())


tree = a
q = deque([tree])
q.appendleft(0)
cnt = 0


# 그래프
graph = {key: val+1 for key, val in enumerate(q)}





# 노드 삭제



# 리프 노드 찾기
def find_leaf(node):






def dfs():
    
    if 

    

































# import sys

# # 리프 노드 찾는 함수
# def find_leaf(node):
#     global answer, checked, delete_node

#     # 현재 노드가 삭제한 노드라면 종료
#     if node == delete_node:
#         return

#     # 현재 노드에 연결된 다른 노드가 없다면 해당 노드가 리프 노드
#     if len(graph[node]) == 0:
#         answer += 1
#         return

#     # 현재 노드에 연결된 다른 노드 탐색
#     for nxt in graph[node]:
#         if checked[nxt]:
#             continue

#         checked[nxt] = True
#         find_leaf(nxt)


# # 노드 개수
# N = int(sys.stdin.readline().rstrip())
# # 입력 받은 정보
# tree = list(map(int, sys.stdin.readline().rstrip().split()))

# root = -1 # 루트 노드 번호
# # 트리 구조 저장할 그래프
# graph = [[] for _ in range(N + 1)]
# for node in range(N):
#     p = tree[node]

#     # 루트 노드 번호 찾기
#     if p == -1:
#         root = node
#         continue

#     graph[p].append(node)

# # 삭제할 노드 번호
# delete_node = int(sys.stdin.readline().rstrip())
# # 삭제할 노드 번호는 삭제해줌
# graph[delete_node] = []

# # 다른 그래프에 저장되어 있는 삭제 노드 번호를 삭제 해 줌
# for g in graph:
#     if delete_node in g:
#         g.remove(delete_node)

# checked = [False for _ in range(N)]
# answer = 0

# checked[root] = True
# # 리프 노드 찾기
# find_leaf(root)

# print(answer)
		






# https://wooono.tistory.com/636

# import sys

# # 트리의 노드의 개수
# n = int(sys.stdin.readline())

# # 0번 노드부터 N-1번 노드까지, 각 노드의 부모
# arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# # 지우려는 노드
# remove_node = int(sys.stdin.readline())

# def dfs(delete, arr):

#     # 현재 노드는 지워야하는 노드이므로, -2로 변환
#     arr[delete] = -2

#     for i in range(n):

#         # 지워야하는 노드를 부모로 둔 자식 노드일 경우, 자식 노드를 -2로 변환
#         if (arr[i] == delete):
#             dfs(i, arr)

# # 각 노드의 부모 배열을 탐색하며,
# # 지워야하는 노드와 해당 노드가 부모 노드인 자식 노드들의 값들을 모두 특정 값(-2)으로 변환
# dfs(remove_node, arr)

# # 리프 노드의 개수
# leaf = 0

# # 각 노드의 부모 배열을 다시 한 번 탐색
# for i in range(n):

#     # 값이 -2 가 아니며, 
#     if (arr[i] != -2):

#         # 해당 노드를 부모로 하는 노드가 부모 배열에 없을 경우, 
#         if (i not in arr):

#             # 리프 노드의 개수를 +1
#             leaf += 1

# print(leaf)





# https://jie0025.tistory.com/150 - 오답 코드 // 접근법과 틀린 부분 확인하기

# import sys
# input = sys.stdin.readline

# def dfs(v):
#     visited[v] = -2
#     for i in graph[v]:
#         dfs(i)
            
# n = int(input())
# li = list(map(int, input().split()))

# graph = [[] for _ in range(n)]
# #그래프는 자식을 담은 리스트로서 사용
# # graph [[1,2],[3,4],[],[],[]]
# for i in range(1,n):
#     graph[li[i]].append(i)

# erase = int(input())
# visited = [0] * n

# dfs(erase)

# cnt = 0
# for i in range(n):
#     if visited[i] != -2 and len(graph[i]) != 0:
#         cnt+=1

# print(cnt)




# 1068_트리_dfs_gold5 - 정답 코드

# import sys
# input = sys.stdin.readline

# def dfs(v):
#     tree[v] = -2
#     for i in range(n): #전체 트리 반복
#         if v == tree[i]: # 지우고자 하는 노드 v가  tree[i]에 들어있으면 tree[i]는 v의 자식
#             dfs(i) # i의 자식도 지움
            
# n = int(input())
# tree = list(map(int, input().split())) # [-1, 0, 0, 1, 1]
# erase = int(input())

# dfs(erase)
# cnt = 0

# for i in range(n):
#     if tree[i] != -2 and i not in tree: #-2는 지우는 노드들 // i노드의 자식이 트리 안에 없으면 == 리프노드임
#         cnt+=1

# print(cnt)