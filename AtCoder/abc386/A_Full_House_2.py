arr = [int(el) for el in input().split()]

import collections
c = collections.Counter(arr)

good = True
if len(c) != 2:
    good = False

if good:
    print('Yes')
else:
    print('No')