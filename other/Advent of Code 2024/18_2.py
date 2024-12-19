from helper import read_blocks
from helper import get_pos_numbers_from_line

lines = read_blocks()[0]

N, M = 71, 71
field = [[0] * M for _ in range(N)]

storage = []
for i, line in enumerate(lines):
    y, x = get_pos_numbers_from_line(line)
    storage.append((y, x))
    field[x][y] = 1
    
parent = [[[i, j] for j in range(M)] for i in range(N)]
rank = [[0] * M for _ in range(N)]

def ufind(a_x, a_y):
    if parent[a_x][a_y] != [a_x, a_y]:
        parent[a_x][a_y] = ufind(*parent[a_x][a_y])
    
    return parent[a_x][a_y]

def uunion(a_x, a_y, b_x, b_y):
    par_a = ufind(a_x, a_y)
    par_b = ufind(b_x, b_y)
    if par_a == par_b:
        return
    rank_a = rank[par_a[0]][par_a[1]]
    rank_b = rank[par_b[0]][par_b[1]]
    if rank_a > rank_b:
        parent[par_b[0]][par_b[1]] = par_a
        return
    if rank_b > rank_a:
        parent[par_a[0]][par_a[1]] = par_b
        return
    parent[par_b[0]][par_b[1]] = par_a
    rank[par_a[0]][par_a[1]] += 1

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            continue
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 0:
                uunion(i, j, ni, nj)

for idx in range(len(storage) - 1, -1, -1):
    y, x = storage[idx]
    field[x][y] = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 0:
            uunion(x, y, nx, ny)
    if ufind(0, 0) == ufind(N - 1, M - 1):
        print(','.join([str(el) for el in storage[idx]]))
        break