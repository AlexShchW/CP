import collections

from helper import read_blocks

blocks = read_blocks()

field = []
for line in blocks[0]:
    field.append(list(line))

N, M = len(field), len(field[0])

for i in range(N):
    for j in range(M):
        if field[i][j] == 'S':
            si, sj = i, j
            field[i][j] = '.'
        if field[i][j] == 'E':
            ei, ej = i, j
            field[i][j] = '.'

dist_from_start_to_normal_cells = collections.defaultdict(lambda: float('inf'))
base_dist = None
visited = set()
dist = 0
q = collections.deque([(si, sj)])
visited.add((si, sj))
while q:
    for _ in range(len(q)):
        cur_i, cur_j = q.popleft()
        dist_from_start_to_normal_cells[(cur_i, cur_j)] = min(dist_from_start_to_normal_cells[(cur_i, cur_j)], dist)
        if cur_i == ei and cur_j == ej and base_dist is None:
            base_dist = dist
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or nj < 0 or ni > N or nj > M:
                continue
            if field[ni][nj] == '#':
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj))
    dist += 1

dist_from_end_to_normal_cells = collections.defaultdict(lambda: float('inf'))
visited = set()
dist = 0
q = collections.deque([(ei, ej)])
visited.add((ei, ej))
while q:
    for _ in range(len(q)):
        cur_i, cur_j = q.popleft()
        dist_from_end_to_normal_cells[(cur_i, cur_j)] = min(dist_from_end_to_normal_cells[(cur_i, cur_j)], dist)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or nj < 0 or ni > N or nj > M:
                continue
            if field[ni][nj] == '#':
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj))
    dist += 1


res_set = set()
for i in range(N):
    for j in range(M):
        if field[i][j] == '#':
            continue
        dist_from_start = dist_from_start_to_normal_cells[(i, j)]
        for skipping in range(1, 21):
            for new_i in range(i - skipping, i + skipping + 1):
                for new_j in range(j - skipping, j + skipping + 1):
                    if new_i < 0 or new_j < 0 or new_i >= N or new_j >= M:
                        continue
                    if field[new_i][new_j] == '#':
                        continue
                    if abs(i - new_i) + abs(j - new_j) < 2:
                        continue
                    if abs(i - new_i) + abs(j - new_j) > skipping:
                        continue
                    dist_from_end = dist_from_end_to_normal_cells[(new_i, new_j)]
                    dist_between = abs(i - new_i) + abs(j - new_j)
                    cur_dist = dist_between + dist_from_end + dist_from_start
                    profit = base_dist - cur_dist
                    if profit >= 100:
                        res_set.add(((i, j), (new_i, new_j)))

print(len(res_set))