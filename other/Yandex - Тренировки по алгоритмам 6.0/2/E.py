n = int(input())

a_arr = [int(el) for el in input().split()]

a_arr.sort()

res = []

if n % 2:
    middle = n // 2
else:
    middle = n // 2 - 1

res.append(a_arr[middle])
left, right = middle - 1, middle + 1

while len(res) < n:
    elements_left = n - len(res)
    # 1 indexing here
    if elements_left % 2:
        middle = elements_left // 2 + 1
    else:
        middle = elements_left // 2

    amount_in_left_part = left + 1
    if amount_in_left_part >= middle:
        res.append(a_arr[left])
        left -= 1
    else:
        res.append(a_arr[right])
        right += 1

print(*res)
