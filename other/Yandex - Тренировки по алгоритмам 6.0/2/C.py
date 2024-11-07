n, r = [int(el) for el in input().split()]

d_arr = [int(el) for el in input().split()]

res = 0
left_idx = 0
right_idx = 0

while left_idx < n and right_idx < n:
    while right_idx < n and d_arr[right_idx] - d_arr[left_idx] <= r:
        right_idx += 1
    res += n - right_idx
    left_idx += 1

print(res)
