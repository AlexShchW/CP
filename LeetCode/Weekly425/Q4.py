class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # we get from subtree of node if node is left with k edges, with k - 1 edges
        def f(node, parent):
            diffs = []
            cur_edge = 0
            res = 0
            for ch, w in graph[node]:
                if ch == parent:
                    continue
                left_with_k, left_with_k_1 = f(ch, node)
                res += left_with_k
                diffs.append(max(0, (left_with_k_1 + w - left_with_k)))
            diffs.sort(reverse=True)
            
            res_for_k = res + sum(diffs[:k])
            res_for_k_1 = res + sum(diffs[:k - 1])
            
            return res_for_k, res_for_k_1

        return f(0, -1)[0]
