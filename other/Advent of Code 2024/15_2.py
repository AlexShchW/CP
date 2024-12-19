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
for row in field:
    cur = []
    for el in row:
        if el == '#':
            cur.append('#')
            cur.append('#')
        elif el == 'O':
            cur.append('[')
            cur.append(']')
        elif el == '.':
            cur.append('.')
            cur.append('.')
        elif el == '@':
            cur.append('@')
            cur.append('.')
    F.append(cur)

N, M = len(F), len(F[0])

for i in range(N):
    for j in range(M):
        if F[i][j] == '@':
            si, sj = i, j
            break

ci, cj = si, sj


def can_move_up_down(i, j, up_down):
    to_move = collections.deque([(i, j)])
    while to_move:
        cur_i, cur_j = to_move.popleft()
        if F[cur_i + up_down][cur_j] == '#':
            return False
        if F[cur_i + up_down][cur_j] == '.':
            continue
        if F[cur_i + up_down][cur_j] == '[':
            to_move.append((cur_i + up_down, cur_j))
            to_move.append((cur_i + up_down, cur_j + 1))
            continue
        if F[cur_i + up_down][cur_j] == ']':
            to_move.append((cur_i + up_down, cur_j))
            to_move.append((cur_i + up_down, cur_j - 1))
            continue
    return True

def move_up_down(i, j, up_down):
    if F[i + up_down][j] == '[':
        move_up_down(i + up_down, j, up_down)
    if F[i + up_down][j] == ']':
        move_up_down(i + up_down, j - 1, up_down)
    if F[i + up_down][j + 1] == '[':
        move_up_down(i + up_down, j + 1, up_down)
    F[i][j] = '.'
    F[i][j + 1] = '.'
    F[i + up_down][j] = '['
    F[i + up_down][j + 1] = ']'



for command in commands:
    if command == '>':
        if F[ci][cj + 1] == '#':
            continue
        if F[ci][cj + 1] == '.':
            F[ci][cj + 1] = '@'
            F[ci][cj] = '.'
            cj += 1
            continue
        is_way = None
        dj = cj
        while True:
            if F[ci][dj] == '.':
                is_way = dj 
                break 
            if F[ci][dj] == '#':
                break
            dj += 1
        if is_way is None:
            continue
        F[ci][cj] = '.'
        F[ci][cj + 1] = '@'
        for idx in range(cj + 2, dj + 1):
            if F[ci][idx - 1] == '[':
                F[ci][idx] = ']'
            else:
                F[ci][idx] = '['
        cj += 1
        continue

    if command == '<':
        if F[ci][cj - 1] == '#':
            continue
        if F[ci][cj - 1] == '.':
            F[ci][cj - 1] = '@'
            F[ci][cj] = '.'
            cj -= 1
            continue
        is_way = None
        dj = cj
        while True:
            if F[ci][dj] == '.':
                is_way = dj 
                break 
            if F[ci][dj] == '#':
                break
            dj -= 1
        if is_way is None:
            continue
        F[ci][cj] = '.'
        F[ci][cj - 1] = '@'
        for idx in range(dj, cj - 1):
            if F[ci][idx - 1] == '[':
                F[ci][idx] = ']'
            else:
                F[ci][idx] = '['
        cj -= 1
        continue

    if command == '^':
        if F[ci - 1][cj] == '#':
            continue
        if F[ci - 1][cj] == '.':
            F[ci - 1][cj] = '@'
            F[ci][cj] = '.'
            ci -= 1
            continue

        if not can_move_up_down(ci, cj, -1):
            continue
        if F[ci - 1][cj] == '[':
            move_up_down(ci - 1, cj, -1)
        elif F[ci - 1][cj] == ']':
            move_up_down(ci - 1, cj - 1, -1)
        
        F[ci][cj] = '.'
        F[ci - 1][cj] = '@'
        ci -= 1

    if command == 'v':
        if F[ci + 1][cj] == '#':
            continue
        if F[ci + 1][cj] == '.':
            F[ci + 1][cj] = '@'
            F[ci][cj] = '.'
            ci += 1
            continue

        if not can_move_up_down(ci, cj, 1):
            continue
        if F[ci + 1][cj] == '[':
            move_up_down(ci + 1, cj, 1)
        elif F[ci + 1][cj] == ']':
            move_up_down(ci + 1, cj - 1, 1)
        
        F[ci][cj] = '.'
        F[ci + 1][cj] = '@'
        ci += 1


res = 0

for i in range(N):
    for j in range(M):
        if F[i][j] == '[':
            res += i * 100 + j 

print(res)