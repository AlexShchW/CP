import collections
import heapq
import sys

from helper import read_blocks
from helper import get_pos_numbers_from_line
from helper import get_strict_words_from_line
from helper import get_words_from_line

sys.setrecursionlimit(10 ** 6)

blocks = read_blocks()

block = blocks[0]

s = collections.defaultdict(set)
for line in block:
    a, b = line.split('-')
    s[a].add(b)
    s[b].add(a)

r = set()
for k in s:
    for k1 in s:
        if k1 == k:
            continue
        for k2 in s:
            if k2 == k or k2 == k1:
                continue
            if k1 in s[k] and k2 in s[k] and k1 in s[k2]:
                if k1[0] == 't' or k2[0] == 't' or k[0] == 't':
                    r.add(tuple(sorted([k1, k2, k])))
print(len(r))