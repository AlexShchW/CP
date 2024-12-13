import collections

field = []
storage = collections.defaultdict(list)

while True:
    try:
        line = input()
        if line == '':
            break
        field.append(list(line))
    except EOFError:
        break

N, M = len(field), len(field[0])

for i in range(N):
    for j in range(M):
        if field[i][j] != '.':
            storage[field[i][j]].append((i, j))

res_set = set()
d = False
for i in range(N):
    for j in range(M):
        el = field[i][j]
        if el == '.':
            continue
        for _i, _j in storage[el]:
            if _i == i and _j == j:
                continue
            di = _i - i
            dj = _j - j
            k = 1
            while True:
                p_1_i, p_1_j = _i + k * di, _j + k * dj
                if 0 <= p_1_i < N and 0 <= p_1_j < M:
                    res_set.add((p_1_i, p_1_j))
                    k += 1
                    continue
                break
            di = -di
            dj = -dj
            k = 1
            while True:
                p_1_i, p_1_j = i + k * di, j + k * dj
                if 0 <= p_1_i < N and 0 <= p_1_j < M:
                    res_set.add((p_1_i, p_1_j))
                    k += 1
                    continue
                break

for i in range(N):
    for j in range(M):
        if field[i][j] != '.' and (i, j) not in res_set:
            res_set.add((i, j))

print(len(res_set))