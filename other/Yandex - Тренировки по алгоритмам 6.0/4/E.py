import collections
import sys

sys.setrecursionlimit(100000)

V = int(input())
tree = collections.defaultdict(set)
for _ in range(V - 1):
    u, v = [int(el) for el in input().split()]
    tree[u].add(v)
    tree[v].add(u)


subtree_sizes = {}

def rec(cur, parent):
    if cur in subtree_sizes:
        return subtree_sizes[cur]
    subtree_sizes[cur] = 1
    for child in tree[cur]:
        if child == parent:
            continue
        subtree_sizes[cur] += rec(child, cur)
    return subtree_sizes[cur]

rec(1, -1)

sorted_nodes = sorted(subtree_sizes.keys())

print(*[subtree_sizes[node] for node in sorted_nodes])

