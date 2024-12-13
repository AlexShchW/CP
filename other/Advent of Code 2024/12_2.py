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
    perimiter_cells = set()
    for cur_i, cur_j in cur_component:
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_i, nxt_j = cur_i + di, cur_j + dj
            if (nxt_i, nxt_j) not in cur_component:
                perimiter_cells.add((cur_i, cur_j))
    
    horizontal_at_i_upper = collections.defaultdict(set)
    horizontal_at_i_lower = collections.defaultdict(set)
    vertical_at_j_left = collections.defaultdict(set)
    vertical_at_j_right = collections.defaultdict(set)

    for cur_i, cur_j in perimiter_cells:
        # left
        if (cur_i, cur_j - 1) not in cur_component:
            vertical_at_j_left[cur_j].add((cur_i, cur_i + 1))
        # right
        if (cur_i, cur_j + 1) not in cur_component:
            vertical_at_j_right[cur_j + 1].add((cur_i, cur_i + 1))
        # top
        if (cur_i - 1, cur_j) not in cur_component:
            horizontal_at_i_upper[cur_i].add((cur_j, cur_j + 1))
        # bottom
        if (cur_i + 1, cur_j) not in cur_component:
            horizontal_at_i_lower[cur_i + 1].add((cur_j, cur_j + 1))
    
    sides = 0
    for i in horizontal_at_i_upper:
        tmp_arr = sorted(horizontal_at_i_upper[i])
        sides += 1
        for idx in range(1, len(tmp_arr)):
            if tmp_arr[idx][0] - tmp_arr[idx - 1][1] > 0:
                sides += 1

    for i in horizontal_at_i_lower:
        tmp_arr = sorted(horizontal_at_i_lower[i])
        sides += 1
        for idx in range(1, len(tmp_arr)):
            if tmp_arr[idx][0] - tmp_arr[idx - 1][1] > 0:
                sides += 1
    
    for j in vertical_at_j_left:
        tmp_arr = sorted(vertical_at_j_left[j])
        sides += 1
        for idx in range(1, len(tmp_arr)):
            if tmp_arr[idx][0] - tmp_arr[idx - 1][1] > 0:
                sides += 1

    for j in vertical_at_j_right:
        tmp_arr = sorted(vertical_at_j_right[j])
        sides += 1
        for idx in range(1, len(tmp_arr)):
            if tmp_arr[idx][0] - tmp_arr[idx - 1][1] > 0:
                sides += 1

    return area * sides

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        res += get_res(i, j)

print(res)