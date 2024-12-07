import collections
import math

N, M, K = [int(el) for el in input().split()]


def solve():
    res = 1
    singles = 0
    friend_groups = 0

    for node in range(1, N + 1):
        if visited[node]:
            continue
        visited[node] = True
        if graph[node]:
            friend_groups += 1
        else:
            singles += 1
            continue
        last_node = node
        q = collections.deque([(node, -1)])
        while q:
            cur_node, parent = q.popleft()
            for neighbour in graph[cur_node]:
                if neighbour == parent:
                    continue
                if visited[neighbour]:
                    return 0
                visited[neighbour] = True
                q.append((neighbour, cur_node))
                last_node = neighbour

        for neighbour in graph[last_node]:
            if len(graph[neighbour]) > 1:
                cur_active_node = neighbour
                break
        else:
            continue # simple case with just 2 nodes
        
        prev_active_node = -1
        up_or_down_processed = False
        while True:
            next_active_node = None
            for neighbour in graph[cur_active_node]:
                if neighbour == prev_active_node:
                    continue
                if len(graph[neighbour]) > 1:
                    if next_active_node is not None:
                        return 0
                    next_active_node = neighbour

            total_valid_neighbours = len(graph[cur_active_node]) - 1
            if prev_active_node == -1:
                total_valid_neighbours += 1

            if next_active_node is None:
                res *= factorial[total_valid_neighbours]
                res %= K
                break

            if not up_or_down_processed:
                res *= 2
                res %= K
                up_or_down_processed = True
            
            res *= factorial[total_valid_neighbours - 1]
            res %= K
            prev_active_node = cur_active_node
            cur_active_node = next_active_node

    res *= pow(2, friend_groups, K) # left / right
    res %= K
    res *= factorial[friend_groups] # which is higher / lower
    res %= K
    if not singles:
        return res


    places = N - singles + 2
    res *= math.perm(places + singles - 1, singles)
    res %= K
    return res

if M >= N:
    print(0)
    
else:
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = [int(el) for el in input().split()]
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    factorial = [1] * (N + 1)
    for i in range(2, N + 1):
        factorial[i] = (factorial[i - 1] * i) % K
    
    print(solve())