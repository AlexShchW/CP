import collections

field = []

while True:
    try:
        line = input()
        if line == '':
            break
        field.append(list(line))
    except EOFError:
        break

N, M = len(field), len(field[0])

visited = [[False] * M for _ in range(N)]

res = 0

def get_res(i, j):
    visited[i][j] = True
    cur_component = set()
    cur_component.add((i, j))
    cur_letter = field[i][j]
    q = collections.deque([(i, j)])
    while q:
        cur_i, cur_j = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_i, nxt_j = cur_i + di, cur_j + dj
            if 0 <= nxt_i < N and 0 <= nxt_j < M and not visited[nxt_i][nxt_j] and field[nxt_i][nxt_j] == cur_letter:
                visited[nxt_i][nxt_j] = True
                cur_component.add((nxt_i, nxt_j))
                q.append((nxt_i, nxt_j))
    
    area = len(cur_component)
    perimeter = 0
    for cur_i, cur_j in cur_component:
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_i, nxt_j = cur_i + di, cur_j + dj
            if (nxt_i, nxt_j) not in cur_component:
                perimeter += 1
    
    return area * perimeter

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        res += get_res(i, j)

print(res)