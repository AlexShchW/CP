# MODE = 'file'
MODE = 'stdin'

if MODE == 'file':
    with open('input.txt', 'r') as file:
        line = file.readline().strip()
else:
    line = input().strip()

line = [int(el) for el in list(line)]

arr = []
cur_idx = 1
is_file = True

for el in line:
    if is_file:
        arr += [cur_idx] * el 
        cur_idx += 1
    else:
        arr += [0] * el
    is_file = not is_file

N = len(arr)
right = N - 1

while right > 0:
    if arr[right] == 0:
        right -= 1
        continue
    file_volume = 1
    right_saved = right
    while right - 1 >= 0 and arr[right - 1] == arr[right]:
        right -= 1
        file_volume += 1
    needs = file_volume
    left = 0
    have = 0
    have_at = None
    while left < right:
        if arr[left] != 0:
            have = 0
            left += 1
            continue
        have += 1
        if have == needs:
            have_at = left
            break
        left += 1
    if have_at is None:
        right -= 1
        continue
    free_spase_start = have_at - needs + 1
    free_space_end = have_at
    for idx in range(free_spase_start, free_space_end + 1):
        arr[idx] = arr[right_saved]
    for idx in range(right, right_saved + 1):
        arr[idx] = 0
    right -= 1


res = 0
for i, el in enumerate(arr):
    if not el:
        continue
    res += i * (el - 1)

print(res)
