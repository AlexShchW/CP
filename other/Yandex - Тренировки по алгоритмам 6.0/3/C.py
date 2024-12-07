import collections

n, k = [int(el) for el in input().split()]

arr = [int(el) for el in input().split()]

poss_mins = collections.deque()

for i in range(k):
    while poss_mins and poss_mins[-1][0] >= arr[i]:
        poss_mins.pop()
    poss_mins.append((arr[i], i))

print(poss_mins[0][0])

left, right = 0, k

while right < n:
    while poss_mins and poss_mins[-1][0] >= arr[right]:
        poss_mins.pop()
    poss_mins.append((arr[right], right))
    while poss_mins[0][1] <= left:
        poss_mins.popleft()
    print(poss_mins[0][0])
    left += 1
    right += 1
