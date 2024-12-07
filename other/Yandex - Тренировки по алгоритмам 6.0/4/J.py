import sys
import math

sys.setrecursionlimit(10 ** 4)

M = 10 ** 9 + 7

N = int(input())

graph = [[] for _ in range(N)]
# [(neighbor, original_target)]
for _ in range(N - 1):
    from_node, to_node = [int(el) - 1 for el in input().split()]
    graph[from_node].append((to_node, to_node))
    graph[to_node].append((from_node, to_node))

dp_results = [[[0] * 2 for _ in range(N + 1)] for _ in range(N)]
# [node][subtree_size][num_reversed_edges_parity]

subtree_sizes = [0] * N
current_dp = [[0] * 2 for _ in range(N + 1)]
next_dp = [[0] * 2 for _ in range(N + 1)]

'''pascal_triangle = [[0] * (N + 1) for _ in range(N + 1)]
pascal_triangle[0][0] = 1
for i in range(N + 1):
    for j in range(N + 1):
        if i:
            pascal_triangle[i][j] += pascal_triangle[i-1][j]
        if i and j:
            pascal_triangle[i][j] += pascal_triangle[i-1][j-1]
        pascal_triangle[i][j] %= M'''


def solve():

    def dfs(current_node, parent_node):
        subtree_sizes[current_node] = 1
        children = []
        # [(child_node, is_original_edge_target)]
        
        for neighbor, original_target in graph[current_node]:
            if neighbor != parent_node:
                dfs(neighbor, current_node)
                subtree_sizes[current_node] += subtree_sizes[neighbor]
                children.append((neighbor, original_target == neighbor))
        
        for size in range(subtree_sizes[current_node] + 1):
            for parity in range(2):
                current_dp[size][parity] = 0
        current_dp[1][0] = 1
        current_size = 1
        
        for child_node, is_original_target in children:
            for arranged_nodes in range(1, current_size + 1):
                for current_parity in range(2):
                    # Can keep original edge direction (if is_original_target) or flip
                    for keep_direction in range(is_original_target, 2):
                        needs_parity_flip = (keep_direction and not is_original_target)
                        
                        for child_size in range(1, subtree_sizes[child_node] + 1):
                            for child_parity in range(2):

                                if keep_direction:
                                    # Merge child's arrangement into current
                                    value = current_dp[arranged_nodes][current_parity]
                                    # Ways to distribute remaining nodes
                                    value *= math.comb(current_size - arranged_nodes + subtree_sizes[child_node] - child_size, subtree_sizes[child_node] - child_size)
                                    value %= M
                                    # Ways to choose positions for child's arrangement
                                    value *= math.comb(arranged_nodes + child_size - 1, child_size)
                                    value %= M
                                    new_parity = current_parity ^ child_parity ^ needs_parity_flip
                                    next_dp[arranged_nodes + child_size][new_parity] += value * dp_results[child_node][child_size][child_parity]
                                    next_dp[arranged_nodes + child_size][new_parity] %= M
        
                                else:
                                    # Keep arrangements separate
                                    value = current_dp[arranged_nodes][current_parity]
                                    # Ways to arrange child's nodes
                                    value *= math.comb(subtree_sizes[child_node], child_size)
                                    value %= M
                                    # Ways to distribute positions
                                    value *= math.comb(current_size - arranged_nodes + subtree_sizes[child_node], subtree_sizes[child_node])
                                    value %= M
                                    new_parity = current_parity ^ child_parity
                                    next_dp[arranged_nodes][new_parity] += value * dp_results[child_node][child_size][child_parity]
                                    next_dp[arranged_nodes][new_parity] %= M
            
            current_size += subtree_sizes[child_node]
            for size in range(current_size + 1):
                for parity in range(2):
                    current_dp[size][parity] = next_dp[size][parity]
                    next_dp[size][parity] = 0
        
        for size in range(current_size + 1):
            for parity in range(2):
                dp_results[current_node][size][parity] = current_dp[size][parity]
    
    
    dfs(0, -1)
    
    res = 0
    for size in range(1, subtree_sizes[0] + 1):
        for parity in range(2):
            cur_res = dp_results[0][size][parity]
            cur_res *= math.comb(subtree_sizes[0], size)
            cur_res %= M
            if parity == 0:
                res += cur_res
            else:
                res -= cur_res
            res %= M
    
    return res % M

print(solve())