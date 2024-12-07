#include <iostream>
#include <vector>
#include <stack>
#include <utility>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<vector<int>> tree(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int parent;
        cin >> parent;
        tree[parent].push_back(i + 2);
    }
    
    vector<pair<long long, long long>> storage(N + 1);
    
    stack<pair<int, bool>> st;
    st.push({1, false});
    
    while (!st.empty()) {
        auto [node, children_processed] = st.top();
        st.pop();
        
        if (children_processed) {
            if (tree[node].empty()) {
                storage[node] = {1LL, 1LL};
                continue;
            }
            
            long long total_sum = 0, total_count = 0;
            for (int child : tree[node]) {
                auto [child_sum, child_count] = storage[child];
                total_sum += child_sum;
                total_sum += child_count;
                total_count += child_count;
            }
            total_sum += 1;
            total_count += 1;
            storage[node] = {total_sum, total_count};
        } else {
            st.push({node, true});
            for (int child : tree[node]) {
                st.push({child, false});
            }
        }
    }
    
    for (int i = 1; i <= N; i++) {
        cout << storage[i].first << " ";
    }
    cout << endl;
    
    return 0;
}