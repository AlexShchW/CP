import collections
import heapq
import sortedcontainers

def read_blocks():
    res = []
    cur_block = []
    while True:
        try:
            line = input()
            if line == "":
                if cur_block:
                    res.append(cur_block)
                cur_block = []
                continue
            cur_block.append(line)
        except EOFError:
            if cur_block:
                res.append(''.join(cur_block))
            break
    return res


def get_pos_numbers_from_line(line):
    res = []
    cur = []
    for c in line:
        if c.isdigit():
            cur.append(c)
        elif cur:
            res.append(int("".join(cur)))
            cur = []
    if cur:
        res.append(int("".join(cur)))
    return res

blocks = read_blocks()

field = blocks[0]

commands = ''.join(blocks[1:])
F = []
for el in field:
    F.append(list(el))

N, M = len(F), len(F[0])

for i in range(N):
    for j in range(M):
        if F[i][j] == '@':
            si, sj = i, j
            break

ci, cj = si, sj


for move in commands:
    
    if move == '^':
        ni, nj = ci, cj
        if ni == 0:
            continue
        if F[ni - 1][nj] == '#':
            continue
        if F[ni - 1][nj] == '.':
            F[ni - 1][nj] = '@'
            F[ni][nj] = '.'
            ci -= 1
            continue 
        found = None
        while ni >= 0:
            if F[ni][nj] == '.':
                found = ni 
                break
            if F[ni][nj] == '#':
                break 
            ni -= 1
        if found is None:
            continue
        F[ci][cj] = '.'
        F[ci - 1][nj] = '@'
        F[found][nj] = 'O'
        ci -= 1

    elif move == 'v':
        ni, nj = ci, cj
        if ni == N - 1:
            continue
        if F[ni + 1][nj] == '#':
            continue
        if F[ni + 1][nj] == '.':
            F[ni + 1][nj] = '@'
            F[ni][nj] = '.'
            ci += 1
            continue
        found = None
        while ni < N:
            if F[ni][nj] == '.':
                found = ni
                break
            if F[ni][nj] == '#':
                break
            ni += 1
        if found is None:
            continue
        F[ci][nj] = '.'
        F[ci + 1][nj] = '@'
        F[found][nj] = 'O'
        ci += 1
    
    elif move == '<':
        ni, nj = ci, cj
        if nj == 0:
            continue
        if F[ni][nj - 1] == '#':
            continue
        if F[ni][nj - 1] == '.':
            F[ni][nj - 1] = '@'
            F[ni][nj] = '.'
            cj -= 1
            continue 
        found = None
        while nj >= 0:
            if F[ni][nj] == '.':
                found = nj
                break
            if F[ni][nj] == '#':
                break 
            nj -= 1
        if found is None:
            continue
        F[ni][cj] = '.'
        F[ni][cj - 1] = '@'
        F[ni][found] = 'O'
        cj -= 1
    
    elif move == '>':
        ni, nj = ci, cj
        if nj == M - 1:
            continue
        if F[ni][nj + 1] == '#':
            continue
        if F[ni][nj + 1] == '.':
            F[ni][nj + 1] = '@'
            F[ni][nj] = '.'
            cj += 1
            continue
        found = None
        while nj < M:
            if F[ni][nj] == '.':
                found = nj
                break
            if F[ni][nj] == '#':
                break 
            nj += 1
        if found is None:
            continue
        F[ni][cj] = '.'
        F[ni][cj + 1] = '@'
        F[ni][found] = 'O'
        cj += 1

res = 0
for i in range(N):
    for j in range(M):
        if F[i][j] == 'O':
            res += i * 100 + j

print(res)