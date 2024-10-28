import collections
import heapq
N, M = [int(el) for el in input().split()]
edges = collections.defaultdict(list)
poss = []
for _ in range(M):
    a, b = [int(el) for el in input().split()]
    edges[a].append(b)
    if b == 1:
        poss.append(a)

dist = [float('inf')] * (N + 1)
dist[1] = 0
h = [(0, 1) ]
while h:
    cur_dist, cur = heapq.heappop(h)
    if cur_dist >= dist[cur]:
        continue
    for b in edges[cur]:
        if dist[b] > cur_dist + 1:
            dist[b] = cur_dist + 1
            heapq.heappush(h, (cur_dist + 1, b))

res = float('inf')
for p in poss:
    res = min(res, dist[p] + 1)

print(res if res != float('inf') else -1)
