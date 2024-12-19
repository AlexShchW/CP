from helper import read_blocks
from helper import get_pos_numbers_from_line

blocks = read_blocks()

import collections

N, M = 71, 71

field = [[0] * N for _ in range(M)]

block = blocks[0]
for i in range(1024):
    line = block[i]
    y, x = get_pos_numbers_from_line(line)
    field[x][y] = 1

steps = 0
q = collections.deque([(0, 0)])
visited = set()
visited.add((0, 0))


done = False
while q:
    for _ in range(len(q)):
        cur_x, cur_y = q.popleft()
        if cur_x == N - 1 and cur_y == M - 1:
            print(steps)
            done = True
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_x, nxt_y = cur_x + dx, cur_y + dy
            if 0 <= nxt_x < N and 0 <= nxt_y < M and field[nxt_x][nxt_y] == 0 and (nxt_x, nxt_y) not in visited:
                visited.add((nxt_x, nxt_y))
                q.append((nxt_x, nxt_y))
    if done:
        break
    steps += 1

print(steps)