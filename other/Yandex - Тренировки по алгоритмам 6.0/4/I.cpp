#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> tree;
vector<vector<vector<tuple<long long, long long, long long>>>> storage;

tuple<long long, long long, long long> dfs(int node, int neighbour_idx, int dest) {
    // looking at edge from node to node at neighbour_idx
    // dest: -1 left dummy, 0 real, 1 right dummy
    // returns: longest path, max deepest path, second max deepest path
    // longest path in subtree overall
    // deepest path from node
    if (dest && (neighbour_idx <= 0 || neighbour_idx >= tree[node].size())) {
        return {0, -1, -1};
    }
    
    int dest_idx = dest + 1;
    
    if (get<0>(storage[node][dest_idx][neighbour_idx]) != 0 || 
        get<1>(storage[node][dest_idx][neighbour_idx]) != -1 || 
        get<2>(storage[node][dest_idx][neighbour_idx]) != -1) {
        return storage[node][dest_idx][neighbour_idx];
    }
    
    vector<long long> deepest_paths;
    vector<long long> longest_paths;
    
    if (dest) {
        auto to_real = dfs(tree[node][neighbour_idx].first, 
                          tree[node][neighbour_idx].second, 0);
        auto continue_dest = dfs(node, neighbour_idx + dest, dest);
        
        longest_paths.push_back(get<0>(to_real));
        longest_paths.push_back(get<0>(continue_dest));
        deepest_paths.push_back(get<1>(to_real));
        deepest_paths.push_back(get<2>(to_real));
        deepest_paths.push_back(get<1>(continue_dest));
        deepest_paths.push_back(get<2>(continue_dest));
    } else {
        auto go_left = dfs(node, neighbour_idx - 1, -1);
        auto go_right = dfs(node, neighbour_idx + 1, 1);
        
        longest_paths.push_back(get<0>(go_left));
        longest_paths.push_back(get<0>(go_right));
        deepest_paths.push_back(get<1>(go_left));
        deepest_paths.push_back(get<2>(go_left));
        deepest_paths.push_back(get<1>(go_right));
        deepest_paths.push_back(get<2>(go_right));
    }
    
    long long longest = *max_element(longest_paths.begin(), longest_paths.end());
    sort(deepest_paths.rbegin(), deepest_paths.rend());
    long long deepest = deepest_paths[0];
    long long second_deepest = deepest_paths[1];
    
    if (!dest) {
        longest = max(longest, deepest + second_deepest + 2);
        deepest += 1;
        second_deepest = -1;
    }
    
    storage[node][dest_idx][neighbour_idx] = {longest, deepest, second_deepest};
    return {longest, deepest, second_deepest};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    tree.resize(N);
    for (int i = 0; i < N; i++) {
        tree[i].push_back({-1, -1});
    }
    
    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        // neighbour, idx of self in neighbour's list
        tree[a].push_back({b, (int)tree[b].size()});
        tree[b].push_back({a, (int)tree[a].size() - 1});
    }
    
    storage.resize(N);
    for (int i = 0; i < N; i++) {
        storage[i].resize(3);
        for (int j = 0; j < 3; j++) {
            storage[i][j].resize(tree[i].size(), make_tuple(0, -1, -1));
        }
    }
    
    long long res = 0;
    for (int node = 0; node < N; node++) {
        for (int neighbour_idx = 1; neighbour_idx < tree[node].size(); neighbour_idx++) {
            auto go_to_neighbour = get<0>(dfs(node, neighbour_idx, 0));
            auto go_from_neighbour = get<0>(dfs(tree[node][neighbour_idx].first, 
                                               tree[node][neighbour_idx].second, 0));
            res = max(res, go_to_neighbour * go_from_neighbour);
        }
    }
    
    cout << res << endl;
    return 0;
}