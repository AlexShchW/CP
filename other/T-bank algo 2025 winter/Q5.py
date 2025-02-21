n, s = [int(el) for el in input().split()]

arr = [int(el) for el in input().split()]

dp_starts = [1] * n
l, r = 0, 0
cur = arr[0]
while r + 1 < n:
    if cur + arr[r + 1] > s:
        dp_starts[r + 1] += dp_starts[l]
        cur -= arr[l]
        l += 1
    else:
        r += 1
        cur += arr[r]

res = 0
for i, el in enumerate(dp_starts):
    poss_ends = n - i
    res += el * poss_ends

print(res)