N, M = [int(el) for el in input().split()]

blacks = []
whites = []
for _ in range(M):
    x, y, color = input().split()
    x = int(x)
    y = int(y)
    if color == 'B':
        blacks.append((x, y))
    else:
        whites.append((x, y))

whites.sort()

import heapq
tallest_to_the_right = []

for x, y in blacks:
    heapq.heappush(tallest_to_the_right, (-y, x))

def solve():
    for x, y in whites:
        while tallest_to_the_right and tallest_to_the_right[0][1] < x:
            heapq.heappop(tallest_to_the_right)
        if tallest_to_the_right and -tallest_to_the_right[0][0] >= y:
            return False
    return True
res = solve()

if res:
    print("Yes")
else:
    print("No")