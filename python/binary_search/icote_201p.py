# 이것이 코딩 테스트다. 201p. 떡볶이 떡 만들기

# 입력
# import sys

# N, M = map(int, sys.stdin.readline())
# lst = map(int, sys.stdin.readline())

N, M = 4, 6   # 가게의 떡의 개수 N, 요청한 떡의 길이 M
lst = [19, 15, 10, 17]   # 가게의 떡 재고

lst.sort()
start = 0
end = lst[-1]

answer = 0

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in lst:
        if i > mid:
            result += i - mid
        else:
            continue
    
    if result < M:
        end = mid - 1
    else:  # if result >= M: mid
        start = mid + 1
        answer = mid
        
print(answer)




# 리팩토링

start = 0
end = max(lst)

answer = 0

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in lst:
        if i > mid:
            result += i - mid
    
    if result < M:
        end = mid - 1
    else:  # if result >= M: mid
        answer = mid
        start = mid + 1
        
print(answer)




# if M == N:
#     c = 1
# else:
#     c = (M // N) + 1

# def cut():
    





