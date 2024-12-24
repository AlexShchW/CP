import collections
import heapq
import sys
from functools import cache
from itertools import product

from helper import read_blocks
from helper import get_pos_numbers_from_line
from helper import get_strict_words_from_line
from helper import get_words_from_line

sys.setrecursionlimit(10 ** 6)

def all_sequences(pad):
    N, M = len(pad), len(pad[0])
    button_to_coords = {}
    for row in range(N):
        for col in range(M):
            if pad[row][col] is not None:
                button_to_coords[pad[row][col]] = (row, col)
    
    sequences = {}

    for let1 in button_to_coords:
        for let2 in button_to_coords:
            if let1 == let2:
                sequences[(let1, let2)] = ['A']
                continue
            poss_routes = []
            q = collections.deque([(button_to_coords[let1], [])])
            min_dist = float('inf')
            while q:
                (row, col), route = q.popleft()
                for new_row, new_col, move in [(row - 1, col, '^'), (row + 1, col, 'v'), \
                                               (row, col - 1, '<'), (row, col + 1, '>')]:
                    if new_row < 0 or new_row == N or new_col < 0 or new_col == M:
                        continue
                    if pad[new_row][new_col] is None:
                        continue
                    if pad[new_row][new_col] == let2:
                        if min_dist < len(route) + 1:
                            break
                        min_dist = len(route) + 1
                        poss_routes.append(''.join(route + [move] + ['A']))
                    else:
                        q.append(((new_row, new_col), route + [move]))
                else:
                    continue
                break
            
            sequences[(let1, let2)] = poss_routes
    
    return sequences

num_pad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dir_pad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

num_seqs = all_sequences(num_pad)

dir_seqs = all_sequences(dir_pad)

def use_first(s, seqs):
    options = [seqs[(l1, l2)] for l1, l2 in zip('A' + s, s)]
    return ["".join(el) for el in product(*options)]

'''s = '029A'
r = use_first(s, num_seqs)
for el in r:
    print(el)'''

dir_lens = {key : len(val[0]) for key, val in dir_seqs.items()}
@cache
def use_second(seq, level):
    if level == 1:
        return sum(dir_lens[(l1, l2)] for l1, l2 in zip('A' + seq, seq))
    res = 0
    for l1, l2 in zip('A' + seq, seq):
        res += min(use_second(route, level - 1) for route in dir_seqs[(l1, l2)])
    return res

res = 0

block = read_blocks()[0]

for line in block:
    num = get_pos_numbers_from_line(line)[0]
    inputs_for_second_pad = use_first(line, num_seqs)
    length = float('inf')
    for input in inputs_for_second_pad:
        length = min(length, use_second(input, 2))
    res += length * num

print(res)