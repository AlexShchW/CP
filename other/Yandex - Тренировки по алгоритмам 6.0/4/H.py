import collections
import sys
sys.setrecursionlimit(500000)

N = int(input())

tree = collections.defaultdict(set)

for _ in range(N - 1):
    v, u = [int(el) for el in input().split()]
    tree[v].add(u)
    tree[u].add(v)

costs = [int(el) for el in input().split()]



if N == 1:
    print(costs[0])
    print(1)
    print(1)
else:
    decisions = {}
    storage = [[None] * (N + 1) for _ in range(2)]
    def cost_to_mark_subtree_rooted_at(node, parent_is_marked, parent):
        if storage[parent_is_marked][node] is not None:
            return storage[parent_is_marked][node]
        cost = costs[node - 1]
        if not parent_is_marked:
            res = cost
            decisions[(node, parent_is_marked)] = True
            for child in tree[node]:
                if child == parent:
                    continue
                res += cost_to_mark_subtree_rooted_at(child, 1, node)
            storage[parent_is_marked][node] = res
            return res
    
        res1 = cost
        for child in tree[node]:
            if child == parent:
                continue
            res1 += cost_to_mark_subtree_rooted_at(child, 1, node)
        
        res2 = 0
        for child in tree[node]:
            if child == parent:
                continue
            res2 += cost_to_mark_subtree_rooted_at(child, 0, node)
    
        should_mark = res1 <= res2
        decisions[(node, parent_is_marked)] = should_mark
        storage[parent_is_marked][node] = min(res1, res2)
        return min(res1, res2)

    for node in tree:
        if len(tree[node]) == 1:
            start_node = node
            break
    min_cost = cost_to_mark_subtree_rooted_at(start_node, 1, -1)

    
    marked_nodes = set()
    def get_marked_nodes(node, parent_is_marked, parent):
        if (node, parent_is_marked) not in decisions:
            return
        if decisions[(node, parent_is_marked)]:
            marked_nodes.add(node)
            for child in tree[node]:
                if child == parent:
                    continue
                get_marked_nodes(child, 1, node)
        else:
            for child in tree[node]:
                if child == parent:
                    continue
                get_marked_nodes(child, 0, node)

    get_marked_nodes(start_node, 1, -1)
    print(min_cost, len(marked_nodes))
    print(*marked_nodes)