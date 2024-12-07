#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 1000001;
vector<vector<int>> graph(MAXN);
vector<bool> visited(MAXN);
int fact_mod[MAXN];

void precalc_factorials(int K) {
    fact_mod[0] = 1;
    for(int i = 1; i < MAXN; i++) {
        fact_mod[i] = (1LL * fact_mod[i-1] * i) % K;
    }
}

int solve(int N, int M, int K) {
    int res = 1;
    int singles = 0;
    int friend_groups = 0;

    for (int node = 1; node <= N; ++node) {
        if (visited[node]) continue;
        visited[node] = true;
        
        if (!graph[node].empty()) {
            ++friend_groups;
        } else {
            ++singles;
            continue;
        }

        int last_node = node;
        queue<pair<int,int>> q;
        q.push({node, -1});
        
        while (!q.empty()) {
            auto [cur_node, parent] = q.front();
            q.pop();
            for (int neighbour : graph[cur_node]) {
                if (neighbour == parent) continue;
                if (visited[neighbour]) return 0;
                visited[neighbour] = true;
                q.push({neighbour, cur_node});
                last_node = neighbour;
            }
        }

        int cur_active_node = -1;
        for (int neighbour : graph[last_node]) {
            if (graph[neighbour].size() > 1) {
                cur_active_node = neighbour;
                break;
            }
        }
        if (cur_active_node == -1) continue;

        int prev_active_node = -1;
        bool up_or_down_processed = false;
        
        while (true) {
            int next_active_node = -1;
            for (int neighbour : graph[cur_active_node]) {
                if (neighbour == prev_active_node) continue;
                if (graph[neighbour].size() > 1) {
                    if (next_active_node != -1) return 0;
                    next_active_node = neighbour;
                }
            }

            int total_valid_neighbours = graph[cur_active_node].size() - 1;
            if (prev_active_node == -1) ++total_valid_neighbours;

            if (next_active_node == -1) {
                res = (1LL * res * fact_mod[total_valid_neighbours]) % K;
                break;
            }

            if (!up_or_down_processed) {
                res = (res * 2) % K;
                up_or_down_processed = true;
            }
            
            res = (1LL * res * fact_mod[total_valid_neighbours - 1]) % K;
            
            prev_active_node = cur_active_node;
            cur_active_node = next_active_node;
        }
    }

    int power_of_2 = 1;
    for (int i = 0; i < friend_groups; ++i) {
        power_of_2 = (power_of_2 * 2) % K;
    }
    res = (1LL * res * power_of_2) % K;

    res = (1LL * res * fact_mod[friend_groups]) % K;
    
    if (!singles) return res;

    int places = N - singles + 2;
    int end = places + singles - 1;
    int start = places - 1;
    for (int i = places; i <= end; ++i) {
        res = (1LL * res * i) % K;
    }
    
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, K;
    cin >> N >> M >> K;
    
    if (M >= N) {
        cout << 0 << '\n';
        return 0;
    }
    
    precalc_factorials(K);
    
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    cout << solve(N, M, K) << '\n';
    return 0;
}