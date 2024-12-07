N, D = [int(el) for el in input().split()]

S = list(input())

idx = N - 1
while idx >= 0 and D > 0:
    if S[idx] == '@':
        D -= 1
        S[idx] = '.'
    idx -= 1

print(''.join(S))