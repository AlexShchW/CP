line = [int(el) for el in list(input())]

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
left = 0
right = N - 1

while left < right:
    while left < right and arr[left] != 0:
        left += 1
    while left < right and arr[right] == 0:
        right -= 1
    if left >= right:
        break
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

res = 0
for i, el in enumerate(arr):
    if not el:
        continue
    res += i * (el - 1)

print(res)