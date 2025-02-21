S = input()

N = len(S)

res = 0
i = 0

while i < N:
    res += 1
    if i + 1 < N and S[i + 1] == S[i] == '0':
        i += 2
    else:
        i += 1

print(res)