N, C = [int(el) for el in input().split()]
T_arr = [int(el) for el in input().split()]

res = 0
cur_time = float('-inf')
for t in T_arr:
    if t - cur_time >= C:
        res += 1
        cur_time = t

print(res)
