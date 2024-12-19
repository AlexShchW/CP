N, M = 103, 101
TIME_ELAPSED = 100

field = [[0] * M for _ in range(N)]

def get_pos(px, py, vx, vy):
    res_x = (px + vx * TIME_ELAPSED) % M
    res_y = (py + vy * TIME_ELAPSED) % N
    return res_x, res_y

while True:
    try:
        line = input()
        if not line:
            break
        p, v = line.split(' ')
        p = p[2:].split(',')
        px = int(p[0])
        py = int(p[1])
        v = v[2:].split(',')
        vx = int(v[0])
        vy = int(v[1])
        
        res_x, res_y = get_pos(px, py, vx, vy)
        field[res_y][res_x] += 1

    except EOFError:
        break

A, B, C, D = 0, 0, 0, 0
for i in range(N // 2):
    for j in range(M // 2):
        A += field[i][j]

for i in range(N // 2 + 1, N):
    for j in range(M // 2):
        B += field[i][j]

for i in range(N // 2):
    for j in range(M // 2 + 1, M):
        C += field[i][j]

for i in range(N // 2 + 1, N):
    for j in range(M // 2 + 1, M):
        D += field[i][j]


print(A * B * C * D)