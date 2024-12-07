field = []
while True:
    try:
        line = input()
        field.append(list(line))
    except EOFError:
        break

N, M = len(field), len(field[0])

for i in range(N):
    for j in range(M):
        if field[i][j] in '^<>v':
            start_row, start_col = i, j

def is_loop():
    cur_row, cur_col = start_row, start_col
    mode = '^'
    visited = set()
    while True:
        if (mode, cur_row, cur_col) in visited:
            return 1
        visited.add((mode, cur_row, cur_col))

        if mode == '^':
            next_row, next_col = cur_row - 1, cur_col
            if next_row < 0:
                return 0
            if field[next_row][next_col] == '#':
                mode = '>'
                continue
            cur_row, cur_col = next_row, next_col
            continue

        if mode == '>':
            next_row, next_col = cur_row, cur_col + 1
            if next_col >= M:
                return 0
            if field[next_row][next_col] == '#':
                mode = 'v'
                continue
            cur_row, cur_col = next_row, next_col
            continue

        if mode == 'v':
            next_row, next_col = cur_row + 1, cur_col
            if next_row >= N:
                return 0
            if field[next_row][next_col] == '#':
                mode = '<'
                continue
            cur_row, cur_col = next_row, next_col
            continue

        if mode == '<':
            next_row, next_col = cur_row, cur_col - 1
            if next_col < 0:
                return 0
            if field[next_row][next_col] == '#':
                mode = '^'
                continue
            cur_row, cur_col = next_row, next_col

res = 0
for i in range(0, N):
    for j in range(0, M):
        if field[i][j] == '#':
            continue
        if i == start_row and j == start_col:
            continue
        field[i][j] = '#'
        res += is_loop()
        field[i][j] = '.'

print(res)
