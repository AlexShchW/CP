N = int(input())
A_arr = [int(el) for el in input().split()]
B_arr = [int(el) for el in input().split()]

A_arr.sort()
B_arr.sort()

def get_res():

    res = 0
    for i in range(N - 1):
        if A_arr[i] > B_arr[i]:
            return -1

    def good(p):
        B = sorted(B_arr[:] + [p])
        for i in range(N):
            if A_arr[i] > B[i]:
                return False
        return True

    l, r = 1, 10 ** 9
    while l <= r:
        p = (l + r) // 2
        if good(p):
            res = p
            r = p - 1
        else:
            l = p + 1
    return res

print(get_res())

