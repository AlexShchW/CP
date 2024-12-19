"""
Register A: ?
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0

1) 2 4
B = A % 8

2) 1 1
B = B ^ 1

3) 7 5
C = A // (2 ** B)

4) 4 4
B = B ^ C

5) 1 4
B = B ^ 4

6) 0 3
A = A // 8

7) 5 5
print(B % 8)

8) 3 0
if A == 0:
    break
else:
    go again
"""

"""
some initial A, then:
while A:
    B = A % 8
    B = B ^ 1
    C = int(A / (2 ** B))
    B = B ^ C
    B = B ^ 4
    A = int(A / 8)
    print(B % 8)
"""

"""
B = A % 8 = A & 7
B = (A & 7) ^ 1 # last 3 bytes of A, then ^ 1
C = int(A / (2 ** B)) = int(A / 2 ** ((A & 7) ^ 1)) = A >> ((A & 7) ^ 1)
B = B ^ C ^ 4 = ((A & 7) ^ 1) ^ (int(A / 2 ** ((A & 7) ^ 1))) ^ 4 \
B = B ^ C ^ 4 = ((A & 7) ^ 1) ^ 4 ^ (A >> ((A & 7) ^ 1))
print(B % 8) <- this we know
A = int(A / 8)

(((A & 7) ^ 1) ^ 4 ^ (A >> ((A & 7) ^ 1))) & 7 = output

(A & 7) ^ 1 = shift
(shift ^ 4 ^ (A >> shift)) & 7 = output

A >>= 3
"""

def use_initial_A(initial_A):
    A = initial_A
    res = []
    while A:
        shift = (A & 7) ^ 1
        out = (shift ^ 4 ^ (A >> shift)) & 7
        res.append(out)
        A >>= 3
    return res

def use_initial_A_once(initial_A):
    A = initial_A
    shift = (A & 7) ^ 1
    out = (shift ^ 4 ^ (A >> shift)) & 7
    return out

"""
Last A is 0 -> 7
otherwise it wouldn't be last
"""

# for A in range(8):
    # use_initial_A(A)
"""
5
7
6
1
0 <- last A is 4
3
2


meaning prev A is from 4 << 3 to (5 << 3 - 1)
and result of this prev loop is also known
"""
import collections

commands = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0]
q = collections.deque([(0, 7)])
for i in range(len(commands) - 1, 0, -1):
    loop_res = commands[i]
    for _ in range(len(q)):
        min_A, max_A = q.popleft()
        for A in range(min_A, max_A + 1):
            cur_res = use_initial_A_once(A)
            if cur_res == loop_res:
                min_A = A << 3
                max_A = ((A + 1) << 3) - 1
                q.append((min_A, max_A))


res = float('inf')
for min_A, max_A in q:
    for A in range(min_A, max_A + 1):
        cur_res = use_initial_A(A)
        if cur_res == commands:
            res = min(res, A)

print(res)