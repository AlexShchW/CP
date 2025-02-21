def solve():
    N, K = [int(el) for el in input().split()]
    arr = [int(el) for el in input().split()]

    total_xor = 0
    for num in arr:
        total_xor ^= num

    if K == 1:
        return max(arr)
    
    if K == N:
        return total_xor
    
    if K <= N - K:
        max_xor = 0
        stack = [(0, 0, 0)]  # (index, current_xor, depth)

        while stack:
            index, current_xor, depth = stack.pop()
            
            if depth == K:
                max_xor = max(max_xor, current_xor)
            elif depth < K:
                for i in range(index, len(arr)):
                    stack.append((i + 1, current_xor ^ arr[i], depth + 1))

        return max_xor
    
    else:
        K = N - K
        max_xor = 0
        stack = [(0, 0, 0)]  # (index, current_xor, depth)

        while stack:
            index, current_xor, depth = stack.pop()
            
            if depth == K:
                max_xor = max(max_xor, current_xor ^ total_xor)
            elif depth < K:
                for i in range(index, len(arr)):
                    stack.append((i + 1, current_xor ^ arr[i], depth + 1))

        return max_xor


print(solve())