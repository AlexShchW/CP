n = int(input())

a_arr = [int(el) for el in input().split()]

pref_sums = [0] * (n + 1)
for i in range(n):
    pref_sums[i + 1] = pref_sums[i] + a_arr[i]

suff_sums = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suff_sums[i] = suff_sums[i + 1] + a_arr[i]

cur_res = 0
for i in range(1, n):
    cur_res += a_arr[i] * i

res = cur_res
for openspace_idx in range(1, n):
    cur_res = cur_res + pref_sums[openspace_idx] - suff_sums[openspace_idx]
    res = min(res, cur_res)

print(res)

'''def my_func(n, a_arr):
    pref_sums = [0] * (n + 1)
    for i in range(n):
        pref_sums[i + 1] = pref_sums[i] + a_arr[i]

    suff_sums = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff_sums[i] = suff_sums[i + 1] + a_arr[i]

    cur_res = 0
    for i in range(1, n):
        cur_res += a_arr[i] * i

    res = cur_res
    for openspace_idx in range(1, n):
        cur_res = cur_res + pref_sums[openspace_idx] - suff_sums[openspace_idx]
        res = min(res, cur_res)
    return res

def brute_force(n, a_arr):
    res = float("inf")
    for openspace_idx in range(n):
        cur_res = 0
        for i in range(n):
            cur_res += a_arr[i] * abs(i - openspace_idx)
        res = min(res, cur_res)
    return res

def check():
    for _ in range(100):
        n = randint(1, 25)
        a_arr = [randint(1, 25) for _ in range(n)]
        assert my_func(n, a_arr) == brute_force(n, a_arr)

check()

'''
