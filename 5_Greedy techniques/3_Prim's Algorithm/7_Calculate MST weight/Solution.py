
import heapq

N = 200010
vis = [False] * N
adj = [[] for _ in range(N)]
MST = []  # Stores the edge list of the Minimum Spanning Tree

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def prims(source, n):  # Source is the starting vertex
    ans = 0
    pq = []
    heapq.heappush(pq, (0, source))

    while pq:
        cost, v = heapq.heappop(pq)

        if vis[v]:
            continue

        vis[v] = True

        ans += cost

        for edge in adj[v]:
            if not vis[edge.first]:
                heapq.heappush(pq, (edge.second, edge.first))

    print(ans)

if __name__ == "__main__":
    n, m = map(int, input().split())

    for i in range(m):
        x, y, w = map(int, input().split())
        adj[x].append(Pair(y, w))
        adj[y].append(Pair(x, w))

    prims(1, n)





