import heapq

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

while h:
    cost, i, j, d = heapq.heappop(h)
    if field[i][j] == 'E':
        print(cost)
        break

    # go forward 
    new_i, new_j = i + d4[d][0], j + d4[d][1]
    if 0 <= new_i < N and 0 <= new_j < M and field[new_i][new_j] != '#':
        new_cost = cost + 1
        if (new_i, new_j, d) not in storage or new_cost < storage[(new_i, new_j, d)]:
            storage[(new_i, new_j, d)] = new_cost
            heapq.heappush(h, (new_cost, new_i, new_j, d))

    # turn left
    new_d = (d - 1) % 4
    new_cost = cost + 1000
    if (i, j, new_d) not in storage or new_cost < storage[(i, j, new_d)]:
        storage[(i, j, new_d)] = new_cost
        heapq.heappush(h, (new_cost, i, j, new_d))

    # turn right
    new_d = (d + 1) % 4
    new_cost = cost + 1000
    if (i, j, new_d) not in storage or new_cost < storage[(i, j, new_d)]:
        storage[(i, j, new_d)] = new_cost
        heapq.heappush(h, (new_cost, i, j, new_d))

