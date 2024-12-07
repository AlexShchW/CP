N, M = [int(el) for el in input().split()]

res = []

cur_sequence = []

def get_poss_starts():
    poss_starts = []
    for i in range(1, M + 1):
        if i + 10 * (N - 1) <= M:
            poss_starts.append(i)
        else:
            break
    return poss_starts


def go():
    if len(cur_sequence) == N:
        res.append(cur_sequence.copy())
        return
    if not cur_sequence:
        for poss_start in get_poss_starts():
            cur_sequence.append(poss_start)
            go()
            cur_sequence.pop()
    
    else:
        cur_number = cur_sequence[-1]
        for poss_next in range(cur_number + 10, M + 1):
            if poss_next + 10 * (N - len(cur_sequence) - 1) <= M:
                cur_sequence.append(poss_next)
                go()
                cur_sequence.pop()

go()
print(len(res))
for sequence in res:
    print(*sequence)
        