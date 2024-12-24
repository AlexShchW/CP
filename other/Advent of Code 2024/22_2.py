import collections
import heapq
import sys

from helper import read_blocks
from helper import get_pos_numbers_from_line
from helper import get_strict_words_from_line
from helper import get_words_from_line

sys.setrecursionlimit(10 ** 6)

block = read_blocks()[0]

res = 0

def get_next(cur):
    tmp = cur * 64
    cur = cur ^ tmp
    cur = cur % 16777216
    tmp = int(cur / 32)
    cur = cur ^ tmp
    cur = cur % 16777216
    tmp = cur * 2048
    cur = cur ^ tmp
    cur = cur % 16777216
    return cur

def f(num):
    for _ in range(2000):
        num = get_next(num)
    return num

def process(num):
    storage = {}
    prev = num % 10
    diffs = collections.deque()
    for _ in range(2000):
        num = get_next(num)
        cur = num % 10
        diffs.append(cur - prev)
        prev = cur
        if len(diffs) == 5:
            diffs.popleft()
        tup = tuple(diffs)
        if tup in storage:
            continue
        storage[tup] = cur
    return storage
res = 0

S = []
for line in block:
    num = get_pos_numbers_from_line(line)[0]
    st = process(num)
    S.append(st)


keys = set()
for st in S:
    keys.update(set(st.keys()))

res = float('-inf')

for key in keys:
    cur_res = 0
    for st in S:
        if key in st:
            cur_res += st[key]
    res = max(res, cur_res)

print(res)