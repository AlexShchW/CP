n, m = [int(el) for el in input().split()]

must_run_this_or_more,  must_run_this_or_less, *arr = [int(el) for el in input().split()]

arr.sort()

left_day_idx = 0
right_day_idx = m - 1

res = float('inf')

while right_day_idx < len(arr):
    adjust_first_day = max(0, must_run_this_or_more - arr[left_day_idx])
    adjust_second_day = max(0, arr[right_day_idx] - must_run_this_or_less)
    res = min(res, adjust_first_day + adjust_second_day)
    left_day_idx += 1
    right_day_idx += 1

print(res)