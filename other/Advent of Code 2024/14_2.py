import collections

N, M = 103, 101

field = [[0] * M for _ in range(N)]

def get_pos(px, py, vx, vy, time_elapsed):
    res_x = (px + vx * time_elapsed) % M
    res_y = (py + vy * time_elapsed) % N
    return res_x, res_y

storage = collections.deque()

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
        storage.append([px, py, vx, vy])
        field[py][px] += 1
    except EOFError:
        break

def check():
    for px, py, _, __ in storage:
        if py + 4 < N and px + 4 < M:
            for right_shift in range(4):
                for down_shift in range(4):
                    if field[py + down_shift][px + right_shift] == 0:
                        return False
            return True
        return False


time_elapsed = 1
while time_elapsed < 100000:
    for _ in range(len(storage)):
        px, py, vx, vy = storage.popleft()
        field[py][px] -= 1
        nx, ny = get_pos(px, py, vx, vy, 1)
        field[ny][nx] += 1
        storage.append([nx, ny, vx, vy])
    if check():
        break
    time_elapsed += 1

print(time_elapsed)