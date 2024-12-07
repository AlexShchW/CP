import collections

N = int(input())
tree = collections.defaultdict(list)
children = set()
for _ in range(N - 1):
    child, parent = input().split()
    tree[parent].append(child)
    children.add(child)

heights = collections.defaultdict(int)

main_ancestor = next(iter(set(tree.keys()) - children))

heights[main_ancestor] = 0

q = collections.deque([main_ancestor])

while q:
    person = q.popleft()
    for child in tree[person]:
        heights[child] = heights[person] + 1
        q.append(child)

for person in sorted(heights.keys()):
    print(person, heights[person])
