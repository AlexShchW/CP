#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX_N = 3003;
const int M = 1e9 + 7;

inline int mod_add(int a, int b) {
    a = ((ll)a + b) % M;
    if (a < 0) a += M;
    return a;
}

inline int mod_mul(int a, int b) {
    return (a * (ll)b) % M;
}

vector<pair<int, int>> graph[MAX_N];
int dp_results[MAX_N][MAX_N][2];
int subtree_sizes[MAX_N];
int current_dp[MAX_N][2];
int next_dp[MAX_N][2];
int pascal_triangle[MAX_N][MAX_N];

void dfs(int current_node, int parent_node) {
    subtree_sizes[current_node] = 1;
    vector<pair<int, int>> children;
    
    for (auto neighbor : graph[current_node]) {
        int to_node = neighbor.first;
        if (to_node != parent_node) {
            dfs(to_node, current_node);
            subtree_sizes[current_node] += subtree_sizes[to_node];
            children.push_back({to_node, neighbor.second == to_node});
        }
    }
    
    for (int i = 0; i <= subtree_sizes[current_node]; i++) {
        for (int parity = 0; parity < 2; parity++) {
            current_dp[i][parity] = 0;
        }
    }
    current_dp[1][0] = 1;
    int current_size = 1;
    
    for (auto child : children) {
        int child_node = child.first, is_original_target = child.second;
        for (int arranged_nodes = 1; arranged_nodes <= current_size; arranged_nodes++) {
            for (int current_parity = 0; current_parity < 2; current_parity++) {
                for (int keep_direction = is_original_target; keep_direction < 2; keep_direction++) {
                    int needs_parity_flip = (keep_direction && !is_original_target);
                    for (int child_size = 1; child_size <= subtree_sizes[child_node]; child_size++) {
                        for (int child_parity = 0; child_parity < 2; child_parity++) {
                            if (keep_direction) {
                                int value = current_dp[arranged_nodes][current_parity];
                                value = mod_mul(value, pascal_triangle[current_size - arranged_nodes + subtree_sizes[child_node] - child_size][subtree_sizes[child_node] - child_size]);
                                value = mod_mul(value, pascal_triangle[arranged_nodes + child_size - 1][child_size]);
                                next_dp[arranged_nodes + child_size][current_parity ^ child_parity ^ needs_parity_flip] = 
                                    mod_add(next_dp[arranged_nodes + child_size][current_parity ^ child_parity ^ needs_parity_flip], 
                                        mod_mul(value, dp_results[child_node][child_size][child_parity]));
                            } else {
                                int value = current_dp[arranged_nodes][current_parity];
                                value = mod_mul(value, pascal_triangle[subtree_sizes[child_node]][child_size]);
                                value = mod_mul(value, pascal_triangle[current_size - arranged_nodes + subtree_sizes[child_node]][subtree_sizes[child_node]]);
                                next_dp[arranged_nodes][current_parity ^ child_parity] = 
                                    mod_add(next_dp[arranged_nodes][current_parity ^ child_parity], 
                                        mod_mul(value, dp_results[child_node][child_size][child_parity]));
                            }
                        }
                    }
                }
            }
        }
        current_size += subtree_sizes[child_node];
        for (int i = 0; i <= current_size; i++) {
            for (int parity = 0; parity < 2; parity++) {
                current_dp[i][parity] = next_dp[i][parity];
                next_dp[i][parity] = 0;
            }
        }
    }
    
    for (int i = 0; i <= current_size; i++) {
        for (int parity = 0; parity < 2; parity++) {
            dp_results[current_node][i][parity] = current_dp[i][parity];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    
    pascal_triangle[0][0] = 1;
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= N; j++) {
            if (i) pascal_triangle[i][j] = mod_add(pascal_triangle[i][j], pascal_triangle[i-1][j]);
            if (i && j) pascal_triangle[i][j] = mod_add(pascal_triangle[i][j], pascal_triangle[i-1][j-1]);
        }
    }
    
    for (int i = 1; i < N; i++) {
        int from_node, to_node;
        cin >> from_node >> to_node;
        from_node--; to_node--;
        graph[from_node].push_back({to_node, to_node});
        graph[to_node].push_back({from_node, to_node});
    }
    
    dfs(0, -1);
    
    int result = 0;
    for (int size = 1; size <= subtree_sizes[0]; size++) {
        for (int parity = 0; parity < 2; parity++) {
            int value = dp_results[0][size][parity];
            value = mod_mul(value, pascal_triangle[subtree_sizes[0]][size]);
            if (parity == 0) result = mod_add(result, value);
            else result = mod_add(result, M - value);
        }
    }
    
    cout << result << '\n';
    return 0;
}