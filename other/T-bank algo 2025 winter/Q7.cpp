#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const long long inv2 = (MOD + 1) / 2;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (auto& a : arr) cin >> a;

    vector<long long> sums_of_powers(k + 1, 0);
    sums_of_powers[0] = n % MOD;

    for (auto a : arr) {
        sums_of_powers[1] = (sums_of_powers[1] + a) % MOD;
        long long cur_pow = a;
        for (int m = 2; m <= k; m++) {
            cur_pow = cur_pow * a % MOD;
            sums_of_powers[m] = (sums_of_powers[m] + cur_pow) % MOD;
        }
    }

    vector<vector<long long>> binom_coeffs_pascal(k + 1);
    for (int p = 0; p <= k; p++) {
        binom_coeffs_pascal[p].resize(p + 1);
        binom_coeffs_pascal[p][0] = binom_coeffs_pascal[p][p] = 1;
        for (int m = 1; m < p; m++) {
            binom_coeffs_pascal[p][m] = (binom_coeffs_pascal[p-1][m-1] + binom_coeffs_pascal[p-1][m]) % MOD;
        }
    }

    vector<long long> results;
    for (int p = 1; p <= k; p++) {
        long long total = 0;
        for (int m = 0; m <= p; m++) {
            const long long coeff = binom_coeffs_pascal[p][m];
            const long long sum_of_m_pows = sums_of_powers[m];
            const long long sum_of_p_minus_m_pows = sums_of_powers[p - m];
            const long long main_part = (coeff * sum_of_m_pows % MOD) * sum_of_p_minus_m_pows % MOD;
            const long long i_equal_j_part = coeff * sums_of_powers[p] % MOD;
            total = (total + (main_part - i_equal_j_part + MOD)) % MOD;
        }
        results.push_back(total * inv2 % MOD);
    }

    for (auto val : results) {
        cout << val << '\n';
    }

    return 0;
}