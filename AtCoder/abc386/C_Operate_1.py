K = int(input())

S = input()
T = input()

def solve():
    if S == K:
        return True
    if len(S) == len(T):
        wrong_met = False
        for i in range(len(S)):
            if S[i] != T[i]:
                if wrong_met:
                    return False
                wrong_met = True
        return True
    if len(S) == len(T) + 1:
        wrong_met = False
        si = 0
        ti = 0
        while si < len(S) and ti < len(T):
            if S[si] == T[ti]:
                si += 1
                ti += 1
                continue
            if wrong_met:
                return False
            wrong_met = True
            si += 1
        return True
    if len(S) == len(T) - 1:
        wrong_met = False
        si = 0
        ti = 0
        while si < len(S) and ti < len(T):
            if S[si] == T[ti]:
                si += 1
                ti += 1
                continue
            if wrong_met:
                return False
            wrong_met = True
            ti += 1
        return True
    return False

res = solve()
if res:
    print("Yes")
else:
    print("No")

    