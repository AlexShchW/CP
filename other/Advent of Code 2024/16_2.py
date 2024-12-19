import heapq
import collections

field = []

while True:
    try:
        line = input()
        if line == '':
            break
        field.append(list(line))
    except EOFError:
        break

N, M = len(field), len(field[0])

for i in range(N):
    for j in range(M):
        if field[i][j] == 'S':
            si, sj = i, j
            break
        
# east, north, west, south
d4 = [(0, -1), (-1, 0), (0, 1), (1, 0)]
sd = 0

storage = {}
storage[(si, sj, sd)] = 0

h = [(0, si, sj, sd)]

prev = collections.defaultdict(set)
while h:
    cost, i, j, d = heapq.heappop(h)
    if field[i][j] == 'E':
        ei, ej, ed = i, j, d
        break

    # go forward 
    new_i, new_j = i + d4[d][0], j + d4[d][1]
    if 0 <= new_i < N and 0 <= new_j < M and field[new_i][new_j] != '#':
        new_cost = cost + 1
        if (new_i, new_j, d) not in storage or new_cost < storage[(new_i, new_j, d)]:
            storage[(new_i, new_j, d)] = new_cost
            heapq.heappush(h, (new_cost, new_i, new_j, d))
            prev[(new_i, new_j, d)].add((i, j, d))
        elif (new_i, new_j, d) in storage and storage[(new_i, new_j, d)] == new_cost:
            prev[(new_i, new_j, d)].add((i, j, d))

    # turn left
    new_d = (d - 1) % 4
    new_cost = cost + 1000
    if (i, j, new_d) not in storage or new_cost < storage[(i, j, new_d)]:
        storage[(i, j, new_d)] = new_cost
        heapq.heappush(h, (new_cost, i, j, new_d))
        prev[(i, j, new_d)].add((i, j, d))
    elif (i, j, new_d) in storage and storage[(i, j, new_d)] == new_cost:
        prev[(i, j, new_d)].add((i, j, d))

    # turn right
    new_d = (d + 1) % 4
    new_cost = cost + 1000
    if (i, j, new_d) not in storage or new_cost < storage[(i, j, new_d)]:
        storage[(i, j, new_d)] = new_cost
        heapq.heappush(h, (new_cost, i, j, new_d))
        prev[(i, j, new_d)].add((i, j, d))
    elif (i, j, new_d) in storage and storage[(i, j, new_d)] == new_cost:
        prev[(i, j, new_d)].add((i, j, d))

res = set()
def go_back(i, j, d):
    res.add((i, j))
    for prev_tup in prev[(i, j, d)]:
        go_back(*prev_tup)

go_back(ei, ej, ed)

print(len(res))