N, Q = [int(el) for el in input().split()]
cur_L, cur_R = 1, 2
res = 0

def dist(a, b):
    return min(abs(a - b), N - abs(a - b))

for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == 'L':
        diff = dist(cur_L, T)
        if diff == dist(cur_L, cur_R) + dist(cur_R, T):
            res += N - diff
        else:
            res += diff
        cur_L = T
    else:
        diff = dist(cur_R, T)
        if diff == dist(cur_L, cur_R) + dist(cur_L, T):
            res += N - diff
        else:
            res += diff
        cur_R = T

print(res)
