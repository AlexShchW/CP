import collections
import sys

sys.setrecursionlimit(100000)
N = int(input())
tree = collections.defaultdict(set)
node_to_parent = {}
for _ in range(N - 1):
    child, parent = input().split()
    tree[parent].add(child)
    node_to_parent[child] = parent

def get_path_to_root(person):
    path = []
    while person in node_to_parent:
        path.append(person)
        person = node_to_parent[person]
    path.append(person)
    return path

def get_lowest_common_ancestor(person1, person2):
    person1_path = get_path_to_root(person1)
    person2_path = set(get_path_to_root(person2))
    for person in person1_path:
        if person in person2_path:
            return person
        

while True:
    try:
        person1, person2 = input().split()
        print(get_lowest_common_ancestor(person1, person2))
    except:
        break

