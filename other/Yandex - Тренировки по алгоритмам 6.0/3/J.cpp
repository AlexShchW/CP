#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <limits>

using namespace std;

int main() {
    int n;
    long long W;
    cin >> n >> W;
    
    vector<long long> h_arr(n), w_arr(n);
    for(int i = 0; i < n; i++) cin >> h_arr[i];
    for(int i = 0; i < n; i++) cin >> w_arr[i];
    
    if(*max_element(w_arr.begin(), w_arr.end()) >= W || n == 1) {
        cout << 0 << endl;
        return 0;
    }

    vector<pair<long long, long long>> combined_arr(n);
    for(int i = 0; i < n; i++) {
        combined_arr[i] = {h_arr[i], w_arr[i]};
    }
    sort(combined_arr.begin(), combined_arr.end());

    vector<long long> diffs(n - 1);
    for(int i = 1; i < n; i++) {
        diffs[i - 1] = combined_arr[i].first - combined_arr[i - 1].first;
    }

    vector<int> idx_of_closest_larger_element_to_the_right(n - 1, -1);
    stack<int> st;
    for(int i = n - 2; i >= 0; i--) {
        while(!st.empty() && diffs[st.top()] <= diffs[i]) {
            st.pop();
        }
        idx_of_closest_larger_element_to_the_right[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    vector<int> idx_of_closest_larger_element_to_the_left(n - 1, -1);
    while(!st.empty()) st.pop();
    for(int i = 0; i < n - 1; i++) {
        while(!st.empty() && diffs[st.top()] <= diffs[i]) {
            st.pop();
        }
        idx_of_closest_larger_element_to_the_left[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    vector<long long> prefix_sums(n);
    long long cur_sum = 0;
    for(int i = 0; i < n; i++) {
        cur_sum += combined_arr[i].second;
        prefix_sums[i] = cur_sum;
    }

    int left = 0, right = 1;
    long long res = numeric_limits<long long>::max();
    while(right < n) {
        long long max_diff_allowed = combined_arr[right].first - combined_arr[left].first;
        int this_diff_idx = left;
        int first_larger_to_the_right_idx = idx_of_closest_larger_element_to_the_right[this_diff_idx];
        int first_larger_to_the_left_idx = idx_of_closest_larger_element_to_the_left[this_diff_idx];
        int last_el_idx = n - 1;
        int first_el_idx = 0;

        if(first_larger_to_the_right_idx != -1) {
            last_el_idx = first_larger_to_the_right_idx;
        }
        if(first_larger_to_the_left_idx != -1) {
            first_el_idx = first_larger_to_the_left_idx + 1;
        }

        long long width = first_el_idx == 0 ? prefix_sums[last_el_idx] : 
                         prefix_sums[last_el_idx] - prefix_sums[first_el_idx - 1];
        
        if(width >= W) {
            res = min(res, max_diff_allowed);
        }
        left++;
        right++;
    }

    cout << res << endl;
    return 0;
}