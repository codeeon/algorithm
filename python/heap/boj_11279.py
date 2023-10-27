# https://www.acmicpc.net/problem/11279

# https://www.notion.so/11279-1a21010374b94015bcbf7e2c6997bb7a?pvs=4



# 1. 최대 힙 구현

from sys import stdin

class BinaryHeap(object):

    def __init__(self):
        self.items = [None]   # 0번 인덱스를 사용하지 않기 위해 만듦.

    def __len__(self):   # 매직 메소드를 이용한 오버라이드 -> len(a) -> a.__len__()
        return len(self.items) - 1   # 0번 인덱스의 None을 새지 않는 느낌

    def _percolate_up(self):   # _는 '내부 함수'라는 표시 - PEP 8 기준, 관례
        i = len(self)
        parent = i // 2   # 루트 인덱스 1 기준, idx → (parent: x, left: 2x, right: 2x+1)
        while parent > 0:
            if self.items[i] > self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()   # 내부 함수로 쓰이는 percolate_up

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        largest = idx

        if left <= len(self) and self.items[left] > self.items[largest]:
            largest = left

        if right <= len(self) and self.items[right] > self.items[largest]:
            largest = right

        if largest != idx:
            self.items[idx], self.items[largest] = self.items[largest], self.items[idx]
            self._percolate_down(largest)   

    def extract(self):
        if len(self) < 1:
            return 0

        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
    

h = BinaryHeap()
x = 0
N = int(stdin.readline())

for i in range(N):
    x = int(stdin.readline())
    
    if x == 0:
        result = h.extract()
        print(result)
    elif x > 0:
        h.insert(x)




# 2. heapq를 활용하여 최대 힙 구현

from sys import stdin
import heapq

h = []
x = 0
N = int(stdin.readline())

for i in range(N):
    x = int(stdin.readline())

    if x > 0:
        heapq.heappush(h, -x)   # heappush(a, b) a에 b 삽입
    elif x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-(heapq.heappop(h)))   # heappop(a) a의 루트 값 추출