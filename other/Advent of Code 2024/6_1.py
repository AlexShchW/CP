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

cur_row, cur_col = start_row, start_col
mode = '^'
visited = set([(start_col, start_row)])
while True:
    if mode == '^':
        next_row, next_col = cur_row - 1, cur_col
        if next_row < 0:
            break
        if field[next_row][next_col] == '#':
            mode = '>'
            continue
        cur_row, cur_col = next_row, next_col
        visited.add((cur_col, cur_row))
        continue

    if mode == '>':
        next_row, next_col = cur_row, cur_col + 1
        if next_col >= M:
            break
        if field[next_row][next_col] == '#':
            mode = 'v'
            continue
        cur_row, cur_col = next_row, next_col
        visited.add((cur_col, cur_row))
        continue

    if mode == 'v':
        next_row, next_col = cur_row + 1, cur_col
        if next_row >= N:
            break
        if field[next_row][next_col] == '#':
            mode = '<'
            continue
        cur_row, cur_col = next_row, next_col
        visited.add((cur_col, cur_row))
        continue

    if mode == '<':
        next_row, next_col = cur_row, cur_col - 1
        if next_col < 0:
            break
        if field[next_row][next_col] == '#':
            mode = '^'
            continue
        cur_row, cur_col = next_row, next_col
        visited.add((cur_col, cur_row))

print(len(visited))
    