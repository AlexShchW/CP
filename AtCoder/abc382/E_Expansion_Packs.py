import sys
import math
sys.setrecursionlimit(10 ** 6)
N, X = [int(el) for el in input().split()]

P_rares = [int(el) / 100 for el in input().split()]


dp = [1] + [0] * N
for p in P_rares:
    new_dp = [0] * (N + 1)
    for j in range(N + 1):
        if j > 0:
            new_dp[j] += dp[j - 1] * p
        new_dp[j] += dp[j] * (1 - p)
    dp = new_dp

rares_amount_probs = {key: prob for key, prob in enumerate(dp)}


# print(rares_amount_probs)

storage = [None] * (N + X)
def expeted_packs(we_have_rares):
    if storage[we_have_rares] is not None:
        return storage[we_have_rares]
    if we_have_rares >= X:
        return 0
    res = 1
    to_mult = 1
    for rares_opened in rares_amount_probs:
        prob = rares_amount_probs[rares_opened]
        if prob == 0:
            continue
        if rares_opened == 0:
            to_mult = 1 - prob
            continue
        if we_have_rares + rares_opened >= X:
            res += 0 
        else:
            res += prob * expeted_packs(we_have_rares + rares_opened)
    res *= (1 / to_mult)
    storage[we_have_rares] = res
    return res

print(expeted_packs(0))