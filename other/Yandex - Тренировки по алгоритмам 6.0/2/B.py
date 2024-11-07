import collections

N, K = [int(el) for el in input().split()]

arr = [int(el) for el in input().split()]

storage = collections.defaultdict(int)
storage[0] = 1

cur_sum = 0
res = 0
for el in arr:
    cur_sum += el
    need = cur_sum - K
    res += storage[need]
    storage[cur_sum] += 1

print(res)

