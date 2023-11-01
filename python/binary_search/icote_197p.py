# 이것이 코딩 테스트다. 197p. 부품 찾기

# import sys

# N = input(int(sys.stdin.readline))
# lst = input(int(sys.stdin.readline))
# M = input(int(sys.stdin.readline))
# buy = input(int(sys.stdin.readline))

N = 5  # 가게의 물품 수
lst = [8, 3, 7, 9, 2]  # 가게의 물품 목록

M = 3  # 구매를 희망하는 물품 수
buy = [5, 7, 9]  # 구매 희망 목록


def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < target:
            start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            return mid
        
    return None


lst.sort()
answer = []

for t in buy:
    result = binary_search(lst, t, 0, N-1)
    if result:
        answer.append('yes')
    else:
        answer.append('no')

print(' '.join(answer))







# N2 = 5  # 가게의 물품 수
# lst2 = [8, 3, 7, 9, 2]  # 가게의 물품 목록

# M2 = 3  # 구매를 희망하는 물품 수
# buy2 = [5, 7, 9]  # 구매 희망 목록

# #

# answer2 = []

# for i in buy2:
#     if i in lst2:
#         answer2.append('yes')
#     else:
#         answer2.append('no')

# print(' '.join(answer2))









# N2 = 5  # 가게의 물품 수
# lst2 = [8, 3, 7, 9, 2]  # 가게의 물품 목록

# M2 = 3  # 구매를 희망하는 물품 수
# buy2 = [5, 7, 9]  # 구매 희망 목록

# #

# for i in buy2:
#     if i in lst2:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')