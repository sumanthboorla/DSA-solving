class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[i].append([j,d])
                adj_list[j].append([i,d])
        
        visited = [0]*n
        pq = [[0,0]]   #dis,node
        heapq.heapify(pq)
        count = 0
        while pq:
            curr = heapq.heappop(pq)
            node = curr[1]
            if not visited[node]:
                visited[node] = 1
                count += curr[0]
                for i in adj_list[node]:
                    if not visited[i[0]]:
                        heapq.heappush(pq,[i[1],i[0]])
        return count
        