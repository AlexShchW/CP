import math
import collections
import heapq

n = int(input())
points = []

for _ in range(n):
    x, y = [int(el) for el in input().split()]
    points.append((x, y))

def get_line(a, b):

    x1, y1 = a
    x2, y2 = b

    if x1 < x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
         return (float('inf'), x1)

    kgcd = math.gcd(abs(dy), abs(dx))
    dx, dy = dx // kgcd, dy // kgcd
    k = (dy, dx)
    if dy == 0:
        k = (0, 1)
    b_numenator = dx * y1 - dy * x1 
    b_denumenator = dx
    if b_numenator == 0:
        b = (0, 1)
    else:
        bgcd = math.gcd(abs(b_numenator), abs(b_denumenator))
        b_numenator, b_denumenator = b_numenator // bgcd, b_denumenator // bgcd
        if b_numenator <= 0 and b_denumenator <= 0:
            b_numenator *= -1
            b_denumenator *= -1
        elif b_numenator >= 0 and b_denumenator <= 0:
            b_numenator *= -1
            b_denumenator *= -1
        b = (b_numenator, b_denumenator)
    return (*k, *b)

lines = collections.defaultdict(set)

for a_idx in range(n):
     for b_idx in range(a_idx + 1, n):
          a = points[a_idx]
          b = points[b_idx]
          line = get_line(a, b)
          lines[line].add(a)
          lines[line].add(b)
          
bad_lines_heap = []
for line in lines:
    if len(lines[line]) >= 3:
        bad_lines_heap.append((-len(lines[line]), line))
heapq.heapify(bad_lines_heap)


processed_points = set()
res = 0

while len(bad_lines_heap) >= 2:
    worst_line_length, worst_line = heapq.heappop(bad_lines_heap)

    worst_point_1 = next(iter(lines[worst_line]))
    lines[worst_line].remove(worst_point_1)
    if worst_point_1 in processed_points:
        worst_line_length += 1
        if worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (worst_line_length, worst_line))
        continue
    
    worst_point_2 = next(iter(lines[worst_line]))
    lines[worst_line].remove(worst_point_2)
    if worst_point_2 in processed_points:
        lines[worst_line].add(worst_point_1)
        worst_line_length += 1
        if worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (worst_line_length, worst_line))
        continue

    worst_point_3 = next(iter(lines[worst_line]))
    lines[worst_line].remove(worst_point_3)
    if worst_point_3 in processed_points:
        lines[worst_line].add(worst_point_1)
        lines[worst_line].add(worst_point_2)
        worst_line_length += 1
        if worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (worst_line_length, worst_line))
        continue
    
    second_worst_line_length, second_worst_line = heapq.heappop(bad_lines_heap)
    
    second_worst_point_1 = next(iter(lines[second_worst_line]))
    lines[second_worst_line].remove(second_worst_point_1)
    if second_worst_point_1 in processed_points:
        second_worst_line_length += 1
        if second_worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (second_worst_line_length, second_worst_line))
        continue
    
    second_worst_point_2 = next(iter(lines[second_worst_line]))
    lines[second_worst_line].remove(second_worst_point_2)
    if second_worst_point_2 in processed_points:
        lines[second_worst_line].add(second_worst_point_1)
        second_worst_line_length += 1
        if second_worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (second_worst_line_length, second_worst_line))
        continue

    second_worst_point_3 = next(iter(lines[second_worst_line]))
    lines[second_worst_line].remove(second_worst_point_3)
    if second_worst_point_3 in processed_points:
        lines[second_worst_line].add(second_worst_point_1)
        lines[second_worst_line].add(second_worst_point_2)
        second_worst_line_length += 1
        if second_worst_line_length <= -3:
            heapq.heappush(bad_lines_heap, (second_worst_line_length, second_worst_line))
        continue

    worst_points = [worst_point_1, worst_point_2, worst_point_3]
    second_worst_points = [second_worst_point_1, second_worst_point_2, second_worst_point_3]

    worst_using = []
    for worst_point in worst_points:
        if worst_point not in lines[second_worst_line]:
            worst_using.append(worst_point)
            if len(worst_points) == 2:
                break

    second_worst_using = None
    for second_worst_point in second_worst_points:
        if second_worst_point not in lines[worst_line]:
            second_worst_using = second_worst_point
            break
    
    res += 1
    processed_points.add(worst_using[0])
    processed_points.add(worst_using[1])
    processed_points.add(second_worst_using)

    for point in second_worst_points:
        if point != second_worst_using:
            lines[second_worst_line].add(point)

    for point in worst_points:
        if point != worst_using[0] and point != worst_using[1]:
            lines[worst_line].add(point)

    worst_line_length += 2
    second_worst_line_length += 1

    if worst_line_length <= -3:
        heapq.heappush(bad_lines_heap, (worst_line_length, worst_line))

    if second_worst_line_length <= -3:
        heapq.heappush(bad_lines_heap, (second_worst_line_length, second_worst_line))

if bad_lines_heap:
    bad_line_points = lines[bad_lines_heap[0][1]]
else:
    bad_line_points = set()

free_points = set()
for point in points:
    if point not in processed_points and point not in bad_line_points:
        free_points.add(point)

free_points_amount = len(free_points)
bad_line_points_amount = len(bad_line_points)
while bad_line_points_amount >= 3:
    if not free_points_amount:
        print(res)
        break
    res += 1
    free_points_amount -= 1
    bad_line_points_amount -= 2
else:
    free_points_amount += bad_line_points_amount
    res += free_points_amount // 3
    print(res)

