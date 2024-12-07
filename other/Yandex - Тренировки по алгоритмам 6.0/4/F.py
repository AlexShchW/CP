import collections

N = int(input())
storage = [int(el) for el in input().split()]

tree = collections.defaultdict(list)

for i, el in enumerate(storage):
    idx = i + 2
    tree[el].append(idx)

storage = [None] * (N + 1)
stack = [(1, 0)]
while stack:
    node, children_processed = stack.pop()
    if children_processed:
        if not tree[node]:
            storage[node] = (1, 1)
            continue
        total_sum, total_count = (0, 0)
        for child in tree[node]:
            child_sum, child_count = storage[child]
            total_sum += child_sum
            total_sum += child_count
            total_count += child_count
        total_sum += 1
        total_count += 1
        storage[node] = (total_sum, total_count)
    else:
        stack.append((node, 1))
        for child in tree[node]:
            stack.append((child, 0))

for i in range(1, N + 1):
    print(storage[i][0], end=' ')

