#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

const int MAXN = 5e5 + 5;
vector<int> tree[MAXN];
vector<long long> costs;
map<pair<int,bool>, bool> decisions;

map<pair<int,bool>, long long> storage;

long long cost_to_mark_subtree_rooted_at(int node, bool parent_is_marked, int parent) {
    auto key = make_pair(node, parent_is_marked);
    if (storage.count(key)) {
        return storage[key];
    }
    
    long long cost = costs[node - 1];
    
    if (!parent_is_marked) {
        long long res = cost;
        decisions[key] = true;
        for (int child : tree[node]) {
            if (child == parent) continue;
            res += cost_to_mark_subtree_rooted_at(child, true, node);
        }
        storage[key] = res;
        return res;
    }
    
    long long res1 = cost;
    for (int child : tree[node]) {
        if (child == parent) continue;
        res1 += cost_to_mark_subtree_rooted_at(child, true, node);
    }
    
    long long res2 = 0;
    for (int child : tree[node]) {
        if (child == parent) continue;
        res2 += cost_to_mark_subtree_rooted_at(child, false, node);
    }
    
    bool should_mark = res1 <= res2;
    decisions[key] = should_mark;
    storage[key] = min(res1, res2);
    return storage[key];
}

void get_marked_nodes(int node, bool parent_is_marked, int parent, set<int>& marked_nodes) {
    auto it = decisions.find({node, parent_is_marked});
    if (it == decisions.end()) return;
    
    if (it->second) {
        marked_nodes.insert(node);
        for (int child : tree[node]) {
            if (child == parent) continue;
            get_marked_nodes(child, true, node, marked_nodes);
        }
    } else {
        for (int child : tree[node]) {
            if (child == parent) continue;
            get_marked_nodes(child, false, node, marked_nodes);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    for (int i = 0; i < n - 1; i++) {
        int v, u;
        cin >> v >> u;
        tree[v].push_back(u);
        tree[u].push_back(v);
    }
    
    costs.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> costs[i];
    }
    
    if (n == 1) {
        cout << costs[0] << "\n1\n1\n";
        return 0;
    }
    
    int start_node = 1;
    for (int i = 1; i <= n; i++) {
        if (tree[i].size() == 1) {
            start_node = i;
            break;
        }
    }
    
    long long min_cost = cost_to_mark_subtree_rooted_at(start_node, true, -1);
    
    set<int> marked_nodes;
    get_marked_nodes(start_node, true, -1, marked_nodes);
    
    cout << min_cost << "\n";
    cout << marked_nodes.size() << "\n";
    for (int node : marked_nodes) {
        cout << node << " ";
    }
    cout << "\n";
    
    return 0;
}