blue_shirts = int(input())
red_shirts = int(input())
blue_socks = int(input())
red_socks = int(input())

def solve():
    if not red_shirts:
        M = 1
        N = red_socks + 1
        return M, N

    if not blue_shirts:
        M = 1
        N = blue_socks + 1
        return M, N

    if not blue_socks:
        N = 1
        M = blue_shirts + 1
        return M, N

    if not red_socks:
        N = 1
        M = red_shirts + 1
        return M, N
    
    serv_arr = []

    # both colors for shirt
    M = max(red_shirts, blue_shirts) + 1
    N = 1
    serv_arr.append((M + N, (M, N)))

    # both colors for socks
    N = max(red_socks, blue_socks) + 1
    M = 1
    serv_arr.append((M + N, (M, N)))

    # guaranteeing red
    M = blue_shirts + 1
    N = blue_socks + 1
    serv_arr.append((M + N, (M, N)))

    # guaranteeing blue
    M = red_shirts + 1
    N = red_socks + 1
    serv_arr.append((M + N, (M, N)))


    return min(serv_arr)[1]

print(*solve())
