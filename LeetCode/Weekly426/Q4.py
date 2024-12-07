class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        tree2 = collections.defaultdict(list)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        
        def we_go_down(node, parent):
            odds = 0
            evens = 1
            for neighbor in tree2[node]:
                if neighbor == parent:
                    continue
                child_odds, child_evens = we_go_down(neighbor, node)
                odds += child_evens
                evens += child_odds
            return odds, evens
        
        res_for_root = we_go_down(0, -1)
        res_for_tree_2 = [None] * m
        res_for_tree_2[0] = res_for_root

        q = collections.deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            for neighbor in tree2[node]:
                if neighbor == parent:
                    continue
                cur_odds, cur_evens = res_for_tree_2[node]
                res_for_tree_2[neighbor] = cur_evens, cur_odds 
                q.append((neighbor, node))

        res_for_tree_2 = set(res_for_tree_2)

        tree1 = collections.defaultdict(list)
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        
        def we_go_down(node, parent):
            odds = 0
            evens = 1
            for neighbor in tree1[node]:
                if neighbor == parent:
                    continue
                child_odds, child_evens = we_go_down(neighbor, node)
                odds += child_evens
                evens += child_odds
            return odds, evens
        
        res_for_root = we_go_down(0, -1)
        res_for_tree_1 = [None] * n
        res_for_tree_1[0] = res_for_root

        q = collections.deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            for neighbor in tree1[node]:
                if neighbor == parent:
                    continue
                cur_odds, cur_evens = res_for_tree_1[node]
                res_for_tree_1[neighbor] = (cur_evens, cur_odds)
                q.append((neighbor, node))
        
        # print(res_for_tree_1, '!!!!!')
        total_res = []
        for odds, evens in res_for_tree_1:
            res = 0
            for poss_odds, poss_evens in res_for_tree_2:
                # res = max(res, odds + poss_evens)
                res = max(res, evens + poss_odds)
            total_res.append(res)
        
        return total_res