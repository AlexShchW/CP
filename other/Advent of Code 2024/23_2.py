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

graph = collections.defaultdict(set)
for line in block:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

cliques = set()

def find_cliques(node, clique):
    clique_tup = tuple(sorted(clique))
    if clique_tup in cliques:
        return
    cliques.add(clique_tup)
    for neigh in graph[node]:
        if neigh in clique:
            continue
        for clique_node in clique:
            if neigh not in graph[clique_node]:
                break
        else:
            updated_clique = clique.copy()
            updated_clique.add(neigh)
            find_cliques(neigh, updated_clique)

for node in graph:
    find_cliques(node, {node})

cliques = sorted(cliques, key=lambda x: len(x), reverse=True)

res = cliques[0]

print(','.join(res))