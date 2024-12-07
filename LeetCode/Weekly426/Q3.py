class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        tree = collections.defaultdict(list)
        for u, v in edges2:
            tree[u].append(v)
            tree[v].append(u)
        
        targets_for_node_in_tree = [0] * m 
        for start_node in range(m):
            visited = [False] * m
            visited[start_node] = True
            res = 0
            dist = 0
            q = collections.deque([(start_node)])
            while q:
                if dist > k - 1:
                    break
                for _ in range(len(q)):
                    cur_node = q.popleft()
                    res += 1
                    for neighbor in tree[cur_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                dist += 1
            targets_for_node_in_tree[start_node] = res
        
        best_target_value = max(targets_for_node_in_tree)


        tree = collections.defaultdict(list)
        for u, v in edges1:
            tree[u].append(v)
            tree[v].append(u)
        
        targets_for_node_in_tree = [0] * n
        for start_node in range(n):
            visited = [False] * n
            visited[start_node] = True
            res = 0
            dist = 0
            q = collections.deque([(start_node)])
            while q:
                if dist > k:
                    break
                for _ in range(len(q)):
                    cur_node = q.popleft()
                    res += 1
                    for neighbor in tree[cur_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                dist += 1
            targets_for_node_in_tree[start_node] = res

        
        return [el + best_target_value for el in targets_for_node_in_tree]