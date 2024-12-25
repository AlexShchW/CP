import collections
import heapq
import sys
import functools

from helper import read_blocks
from helper import get_pos_numbers_from_line
from helper import get_strict_words_from_line
from helper import get_words_from_line

sys.setrecursionlimit(10 ** 6)

blocks = read_blocks()

locks = []
keys = []

for block in blocks:
    n, m = len(block), len(block[0])
    if block[0][0] == '#':
        arr = []
        for j in range(m):
            cur = 0
            for i in range(n):
                if block[i][j] == '#':
                    cur += 1
            arr.append(cur - 1)
        locks.append(arr)
    else:
        arr = []
        for j in range(m):
            cur = 0
            for i in range(n - 1, -1, -1):
                if block[i][j] == '#':
                    cur += 1
            arr.append(cur - 1)
        keys.append(arr)

res = 0
for key in keys:
    for lock in locks:
        fail = False
        for k, l in zip(key, lock):
            if k + l > n - 2:
                fail = True
                break
            if fail:
                break
        if not fail:
            res += 1

print(res)



        