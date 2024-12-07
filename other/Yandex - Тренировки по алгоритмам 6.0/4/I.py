import sys

sys.setrecursionlimit(100010)


def dfs(node, neighbour_idx, dest): 
    # looking at edge from node to node at neighbour_idx
    # dest: -1 left dummy, 0 real, 1 right dummy
    # returns: longest path, max deepest path, second max deepest path
    # longest path in subtree overall
    # deepest path from node
    if dest and (neighbour_idx <= 0 or neighbour_idx >= len(tree[node])):
        return 0, -1, -1
    
    dest_idx = dest + 1

    if storage[node][dest_idx][neighbour_idx][0]:
        return storage[node][dest_idx][neighbour_idx]
    
    deepest_paths = []
    longest_paths = []
    if dest:
        to_real = dfs(tree[node][neighbour_idx][0], tree[node][neighbour_idx][1], 0)
        continue_dest = dfs(node, neighbour_idx + dest, dest)
        longest_paths.append(to_real[0])
        longest_paths.append(continue_dest[0])
        deepest_paths.extend(to_real[1:])
        deepest_paths.extend(continue_dest[1:])
    else:
        go_left = dfs(node, neighbour_idx - 1, -1)
        go_right = dfs(node, neighbour_idx + 1, 1)
        longest_paths.append(go_left[0])
        longest_paths.append(go_right[0])
        deepest_paths.extend(go_left[1:])
        deepest_paths.extend(go_right[1:])
    
    longest = max(longest_paths)
    deepest_paths.sort(reverse=True)
    deepest = deepest_paths[0]
    second_deepest = deepest_paths[1]
    
    if not dest:
        longest = max(longest, deepest + second_deepest + 2)
        deepest += 1
        second_deepest = -1
    
    return longest, deepest, second_deepest

N = int(input())

tree = [[(None, None)] for _ in range(N)]

for _ in range(N - 1):
    a, b = [int(el) - 1 for el in input().split()]
    # neighbour, idx of self in neighbour's list
    tree[a].append((b, len(tree[b])))
    tree[b].append((a, len(tree[a]) - 1))

# storage[node][direction + 1][neighbour_index] = (longest, deepest, second_deepest)
storage = [[[(0, -1, -1) for _ in range(len(tree[i]))] for _ in range(3)] for i in range(N)]

res = 0
for node in range(N):
    for neighbour_idx in range(1, len(tree[node])):
        go_to_neighbour = dfs(node, neighbour_idx, 0)[0]
        go_from_neighbour = dfs(tree[node][neighbour_idx][0], tree[node][neighbour_idx][1], 0)[0]
        res = max(res, go_to_neighbour * go_from_neighbour)

print(res)
