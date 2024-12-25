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

main = blocks[1]
storage = {}
for line in main:
    f, s = line.split('->')
    f = f[:-1]
    s = s[1:]
    a, op, b = f.split()
    storage[s] = (a, op, b)

def gate_name(let, num):
    return let + str(num).rjust(2, '0')

def verify_z(gate, num):
    if gate not in storage:
        return False
    a, op, b = storage[gate]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([a, b]) == ["x00", "y00"]
    return verify_intermidiate_xor(a, num) and verify_carry_bit(b, num) or verify_intermidiate_xor(b, num) and verify_carry_bit(a, num)

def verify_intermidiate_xor(gate, num):
    if gate not in storage:
        return False
    a, op, b = storage[gate]
    if op != "XOR":
        return False
    return sorted([a, b]) == [gate_name('x', num), gate_name('y', num)]

def verify_carry_bit(gate, num):
    if gate not in storage:
        return False
    a, op, b = storage[gate]
    if num == 1:
        if op != "AND":
            return False
        return sorted([a, b]) == ["x00", "y00"]
    if op != "OR":
        return False
    return verify_direct_carry(a, num - 1) and verify_recarry(b, num - 1) or verify_direct_carry(b, num - 1) and verify_recarry(a, num - 1)

def verify_direct_carry(gate, num):
    if gate not in storage:
        return False
    a, op, b = storage[gate]
    if op != "AND":
        return False
    return sorted([a, b]) == [gate_name('x', num), gate_name('y', num)]

def verify_recarry(gate, num):
    if gate not in storage:
        return False
    a, op, b = storage[gate]
    if op != "AND":
        return False
    return verify_intermidiate_xor(a, num) and verify_carry_bit(b, num) or verify_intermidiate_xor(b, num) and verify_carry_bit(a, num)

def verify(num):
    return verify_z(gate_name('z', num), num)

def progress():
    i = 0
    while True:
        if not verify(i):
            return i
        i += 1

res = []
for _ in range(4):
    cur_progress = progress()
    for a in storage:
        for b in storage:
            if a == b:
                continue
            storage[a], storage[b] = storage[b], storage[a]
            if progress() > cur_progress:
                break
            storage[a], storage[b] = storage[b], storage[a]
        else:
            continue
        break
    res.append(a)
    res.append(b)

res.sort()
print(','.join(res))