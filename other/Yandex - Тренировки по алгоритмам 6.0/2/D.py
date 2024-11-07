n, k = [int(el) for el in input().split()]

a_arr = [int(el) for el in input().split()]
a_arr.sort()

cur_bad = 0

left, right = 0, 0
while left < n and right < n:
    if a_arr[right] - a_arr[left] <= k:
        cur_bad = max(cur_bad, right - left + 1)
        right += 1
    else:
        left += 1

print(cur_bad)
