n = int(input())

sums_up_to = [0] * (n + 10)

right_idx = 0
for i in range(n):
    op = input()
    if op[0] == '+':
        num = int(op[1:])
        sums_up_to[right_idx] = sums_up_to[right_idx - 1] + num if right_idx > 0 else num
        right_idx += 1
        continue
    if op[0] == '-':
        print(sums_up_to[right_idx - 1] - sums_up_to[right_idx - 2] if right_idx > 1 else sums_up_to[right_idx - 1])
        right_idx -= 1
        continue
    k = int(op[1:])
    if not k:
        print(0)
        continue
    print(sums_up_to[right_idx - 1] - sums_up_to[right_idx - k - 1] if right_idx - k - 1 >= 0 else sums_up_to[right_idx - 1])
