n = int(input())
a_arr = [int(el) for el in input().split()]

res = []
cur = 0
for el in a_arr:
    cur += el
    res.append(cur)

print(*res)

