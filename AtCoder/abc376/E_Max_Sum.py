import heapq

T = int(input())
for _ in range(T):
    N, K = [int(el) for el in input().split()]
    A_arr = [int(el) for el in input().split()]
    B_arr = [int(el) for el in input().split()]

    arr = [(a, b) for a, b in zip(A_arr, B_arr)]
    arr.sort()
    S = 0
    MA = arr[K - 1][0]
    H = []
    for i in range(K):
        S += arr[i][1]
        heapq.heappush(H, -arr[i][1])
    res = S * MA
    for i in range(K, N):
        new_MA = arr[i][0]
        adding = arr[i][1]
        heapq.heappush(H, -adding)
        got = -heapq.heappop(H)
        S = S - got + adding
        res = min(res, S * new_MA)
    print(res)




