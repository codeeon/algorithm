import heapq

# n = 4  # 노드의 수
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]  # 항공편
# src = 0  # 시작점
# dst = 3  # 도착점
# k = 1  # 경유지 수


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = [[] for _ in range(1+n)]
        for edge in flights:
            graph[edge[0]] += [(edge[2], edge[1])]
        INF = 1e9
        dist = [INF]*(1+n)
        dist[src] = 0

        def djikstra(start):
            heap=[]
            heapq.heappush(heap, (0, start, 0))

            while heap:
                cost, cur, cnt = heapq.heappop(heap) # 비용, 현재 노드, 경유 수

                # 현재 cnt가 k보다 큰 경우 멈추기
                if cnt > k:
                    continue
                
                # 현재 노드에서 갈 수 있는 노드에 대한 반복
                for nxt in graph[cur]:

                    if dist[nxt[1]] < nxt[0]: # 현재 최소 비용보다 다음 노드 비용이 비쌀 때, 패스
                        continue
                
                    ncost = nxt[0] + cost # 새로운 비용

                    if ncost < dist[nxt[1]]:
                        dist[nxt[1]] = ncost
                        heapq.heappush(heap, (ncost, nxt[1], cnt+1))

        djikstra(src)
        if dist[dst] == INF:
            return -1
        else:
            return dist[dst]
            