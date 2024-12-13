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
            p_1_i, p_1_j = _i + di, _j + dj
            di = -di
            dj = -dj
            p_2_i, p_2_j = i + di, j + dj
            if 0 <= p_1_i < N and 0 <= p_1_j < M:
                res_set.add((p_1_i, p_1_j))
            if 0 <= p_2_i < N and 0 <= p_2_j < M:
                res_set.add((p_2_i, p_2_j))


print(len(res_set))