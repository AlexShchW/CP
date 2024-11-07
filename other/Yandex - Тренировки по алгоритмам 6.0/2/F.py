n = int(input())

a_arr = [int(el) for el in input().split()]

M = 10 ** 9 + 7

pref_sums = [0] * (n + 1)

for i in range(1, n + 1):
    pref_sums[i] = pref_sums[i - 1] + a_arr[i - 1]

suff_sums = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    suff_sums[i] = suff_sums[i + 1] + a_arr[i]

res = 0

for middle in range(1, n - 1):
    left_part = pref_sums[middle] % M
    right_part = suff_sums[middle + 1] % M

    res += (a_arr[middle] * left_part * right_part)
    res %= M

print(res)

