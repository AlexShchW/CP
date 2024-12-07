field = []
while True:
    try:
        line = input()
        field.append(list(line))
    except EOFError:
        break
N, M = len(field), len(field[0])
def count_from_here(i, j):
    ms = 0
    ss = 0
    if i - 1 >= 0 and j - 1 >= 0 and i + 1 < N and j + 1 < M:
        if field[i - 1][j - 1] == 'M':
            ms += 1
        if field[i - 1][j + 1] == 'M':
            ms += 1
        if field[i + 1][j - 1] == 'M':
            ms += 1
        if field[i + 1][j + 1] == 'M':
            ms += 1

        if field[i - 1][j - 1] == 'S':
            ss += 1
        if field[i + 1][j - 1] == 'S':
            ss += 1
        if field[i - 1][j + 1] == 'S':
            ss += 1
        if field[i + 1][j + 1] == 'S':
            ss += 1
    if ms == 2 and ss == 2:
        if field[i - 1][j - 1] == 'M' and field[i + 1][j + 1] == 'S':
            return 1
        if field[i - 1][j - 1] == 'S' and field[i + 1][j + 1] == 'M':
            return 1
    return 0

res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'A':
            res += count_from_here(i, j)

print(res)