import collections

field = []

while True:
    try:
        line = list(input())
        field.append([int(el) for el in line])
    except EOFError:
        break

res = 0

N, M = len(field), len(field[0])

def score(i, j):
    res = 0
    q = collections.deque([(0, i, j)])
    while q:
        num, cur_i, cur_j = q.popleft()
        if num == 9:
            res += 1
            continue
        nxt_num = num + 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_i, nxt_j = cur_i + di, cur_j + dj
            if 0 <= nxt_i < N and 0 <= nxt_j < M and field[nxt_i][nxt_j] == nxt_num:
                q.append((nxt_num, nxt_i, nxt_j))
    
    return res


for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            res += score(i, j)

print(res)