N, M = [int(el) for el in input().split()]

gourmet_levels = [int(el) for el in input().split()]

deliciousness_levels = [int(el) for el in input().split()]

deliciousness_levels = sorted([(el, i) for i, el in enumerate(deliciousness_levels)], reverse=True)

cur_gourmet_idx = 0

res = [None] * M

for deliciousness_level, idx in deliciousness_levels:
    while cur_gourmet_idx < N and deliciousness_level < gourmet_levels[cur_gourmet_idx]:
        cur_gourmet_idx += 1
    if cur_gourmet_idx < N:
        res[idx] = cur_gourmet_idx + 1
    else:
        res[idx] = -1

for el in res:
    print(el)