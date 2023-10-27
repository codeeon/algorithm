# https://leetcode.com/problems/kth-largest-element-in-an-array/description/


import heapq


# 1. heapq

def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(1, k):
        heapq.pop(heap)

    return -heapq.pop(heap)
# heapq는 최소 힙을 지원하기 때문에, 음수로 저장하고 낮은 수부터 추출해 부호를 변환하여 최대 힙처럼 동작하도록 구현.


# 2. heapq의 heapify - 자료구조가 힙 특성을 만족하도록 바꿔주는 연산. (이후 한 번 값을 넣으면 특성이 깨짐)

def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


# 3. heapq의 nlargest - n번째 큰 값을 추출하는 기능.

def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


# 4. 정렬을 이용한 풀이

def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]