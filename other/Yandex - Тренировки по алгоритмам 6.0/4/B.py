import collections
import sys

sys.setrecursionlimit(100000)
N = int(input())
tree = collections.defaultdict(list)
children = set()
for _ in range(N - 1):
    child, parent = input().split()
    tree[parent].append(child)
    children.add(child)

amounts_of_children = collections.defaultdict(int)

main_ancestor = next(iter(set(tree.keys()) - children))

def get_amount_of_descendants(person):
    if person not in amounts_of_children:
        if not tree[person]:
            amounts_of_children[person] = 0
        else:
            res = 0
            for child in tree[person]:
                res += get_amount_of_descendants(child)
                res += 1
            amounts_of_children[person] = res
    return amounts_of_children[person]

get_amount_of_descendants(main_ancestor)

for person in sorted(amounts_of_children.keys()):
    print(person, amounts_of_children[person])

