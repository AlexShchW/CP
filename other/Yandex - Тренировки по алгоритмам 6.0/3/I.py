import collections

N = int(input())

a, b = [int(el) for el in input().split()]

all_roads = set(range(1, 5))
main_roads = set([a, b])
sub_roads_list = list(all_roads - main_roads)

def prio(road_number):
    if road_number in main_roads:
        if abs(a - b) == 2:
            return 0
        else:
            another_road = a if road_number == b else b
            if another_road - road_number == 1 or another_road - road_number == -3:
                return 0 
            else:
                return 1
    if abs(a - b) == 2:
        return 3
    another_road = sub_roads_list[0] if road_number == sub_roads_list[1] else sub_roads_list[1]
    if another_road - road_number == 1 or another_road - road_number == -3:
        return 3
    else:
        return 4

prio_1 = prio(1)
prio_2 = prio(2)
prio_3 = prio(3)
prio_4 = prio(4)


_1_q = []
_2_q = []
_3_q = []
_4_q = []

for i in range(N):
    d, t = [int(el) for el in input().split()]
    if d == 1:
        _1_q.append((t, prio_1, i))
    if d == 2:
        _2_q.append((t, prio_2, i))
    if d == 3:
        _3_q.append((t, prio_3, i))
    if d == 4:
        _4_q.append((t, prio_4, i))

_1_q.sort()
_2_q.sort()
_3_q.sort()
_4_q.sort() 

_1_q = collections.deque(_1_q)
_2_q = collections.deque(_2_q)
_3_q = collections.deque(_3_q)
_4_q = collections.deque(_4_q)

res = [None] * N

cur_time = 0
while _1_q or _2_q or _3_q or _4_q:
    ready_to_go = []
    for q in [_1_q, _2_q, _3_q, _4_q]:
        if q and q[0][0] <= cur_time:
            ready_to_go.append(q[0])
    if not ready_to_go:
        cur_time = float('inf')
        for q in [_1_q, _2_q, _3_q, _4_q]:
            if q and q[0][0] < cur_time:
                cur_time = q[0][0]
        for q in [_1_q, _2_q, _3_q, _4_q]:
            if q and q[0][0] == cur_time:
                ready_to_go.append(q[0])
    ready_to_go.sort(key=lambda x: x[1])
    going_arr = [ready_to_go[0]]
    for i in range(1, len(ready_to_go)):
        if ready_to_go[i][1] == ready_to_go[0][1]:
            going_arr.append(ready_to_go[i])
    
    
    for going in going_arr:
        for q in [_1_q, _2_q, _3_q, _4_q]:
            if q and q[0] == going:
                q.popleft()
        res[going[2]] = cur_time
    cur_time += 1
    

for el in res:
    print(el)

