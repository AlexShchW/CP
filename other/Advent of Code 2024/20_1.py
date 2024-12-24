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

dist_from_start_to_obst = collections.defaultdict(lambda: float('inf'))
base_dist = None
visited = set()
dist = 0
q = collections.deque([(si, sj)])
visited.add((si, sj))
while q:
    for _ in range(len(q)):
        cur_i, cur_j = q.popleft()
        if cur_i == ei and cur_j == ej and base_dist is None:
            base_dist = dist
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or nj < 0 or ni > N or nj > M:
                continue
            if field[ni][nj] == '#':
                dist_from_start_to_obst[(ni, nj)] = min(dist_from_start_to_obst[(ni, nj)], 1 + dist)
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj))
    dist += 1

dist_from_end_to_obst = collections.defaultdict(lambda: float('inf'))
visited = set()
dist = 0
q = collections.deque([(ei, ej)])
visited.add((ei, ej))
while q:
    for _ in range(len(q)):
        cur_i, cur_j = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = cur_i + di, cur_j + dj
            if ni < 0 or nj < 0 or ni > N or nj > M:
                continue
            if field[ni][nj] == '#':
                dist_from_end_to_obst[(ni, nj)] = min(dist_from_end_to_obst[(ni, nj)], 1 + dist)
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj))
    dist += 1

res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == '#':
            dist1 = dist_from_end_to_obst[(i, j)]
            dist2 = dist_from_start_to_obst[(i, j)]
            if base_dist - (dist1 + dist2) >= 100:
                res += 1

print(res)

