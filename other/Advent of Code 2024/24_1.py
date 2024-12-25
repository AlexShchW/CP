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

in_vals = blocks[0]

values = {}
for line in in_vals:
    gate, val = line.split()
    gate = gate[:-1]
    val = int(val)
    values[gate] = val

main = blocks[1]

storage = {}
for line in main:
    f, s = line.split('->')
    f = f[:-1]
    s = s[1:]
    a, op, b = f.split()
    storage[s] = (a, op, b)

@functools.cache
def get_val(gate):
    if gate in values:
        return values[gate]
    a, op, b = storage[gate]
    a_val = get_val(a)
    b_val = get_val(b)
    if op == 'AND':
        res = a_val & b_val
    elif op == 'OR':
        res = a_val | b_val
    else:
        res = a_val ^ b_val
    values[gate] = res
    return res

z_arr = []
for gate in storage:
    if gate[0] == 'z':
        z_arr.append((gate, get_val(gate)))

z_arr.sort()

res = 0
i = 0
for gate, val in z_arr:
    res += val * 2 ** i
    i += 1

print(res)