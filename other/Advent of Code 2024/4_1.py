field = []
while True:
    try:
        line = input()
        field.append(list(line))
    except EOFError:
        break
N, M = len(field), len(field[0])
def count_from_here(i, j):
    res = 0
    # go right
    if j + 3 < M:
        if field[i][j : j + 4] == ['X', 'M', 'A', 'S']:
            res += 1
    # go left
    if j - 3 >= 0:
        if field[i][j - 3 : j + 1] == ['S', 'A', 'M', 'X']:
            res += 1
    # go down
    if i + 3 < N:
        tmp = []
        for k in range(4):
            tmp.append(field[i + k][j])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1
    # go up
    if i - 3 >= 0:
        tmp = []
        for k in range(4):
            tmp.append(field[i - k][j])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1

    # go up right
    if i - 3 >= 0 and j + 3 < M:
        tmp = []
        for k in range(4):
            tmp.append(field[i - k][j + k])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1
    # go up left
    if i - 3 >= 0 and j - 3 >= 0:
        tmp = []
        for k in range(4):
            tmp.append(field[i - k][j - k])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1
    # go down right
    if i + 3 < N and j + 3 < M:
        tmp = []
        for k in range(4):
            tmp.append(field[i + k][j + k])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1

    # go down left
    if i + 3 < N and j - 3 >= 0:
        tmp = []
        for k in range(4):
            tmp.append(field[i + k][j - k])
        if tmp == ['X', 'M', 'A', 'S']:
            res += 1

    return res

res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'X':
            res += count_from_here(i, j)

print(res)